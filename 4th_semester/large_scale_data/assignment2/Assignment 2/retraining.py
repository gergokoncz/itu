import pandas as pd
from matplotlib import pyplot as plt
from influxdb import InfluxDBClient
from dateutil.parser import parse
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import KFold, cross_val_score

client = InfluxDBClient(host='influxus.itu.dk', port=8086, username='lsda', password='icanonlyread')
client.switch_database('orkney')

df = pd.DataFrame()
results = client.query('SELECT mean(Total) FROM "Demand" WHERE time > now() - 365d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = pd.concat([df, pd.DataFrame(values,columns=['time', 'demand'])], axis=1)

results = client.query('SELECT mean("M/S") FROM "Wind" WHERE time > now() - 365d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = df.merge(pd.DataFrame(values, columns=['time', 'wind']), on='time')

results = client.query('SELECT mean("u") FROM "Wind" WHERE time > now() - 365d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = df.merge(pd.DataFrame(values, columns=['time', 'u wind']), on='time')

results = client.query('SELECT mean("v") FROM "Wind" WHERE time > now() - 365d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = df.merge(pd.DataFrame(values, columns=['time', 'v wind']), on='time')

results = client.query('SELECT mean(*) FROM "ANM_Operation" WHERE time > now() - 365d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]

df_val = pd.DataFrame()
df_val['time'] = np.array(values)[:,0]
df_val['curtailment'] = np.array(values)[:,0]

for idx, i in enumerate(np.array(values)[:,1:].astype(float)):
    if sum(i) > 1:
        df_val['curtailment'].iloc[idx] = 1
    else:
        df_val['curtailment'].iloc[idx] = 0
df = df.merge(pd.DataFrame(df_val, columns=['time', 'curtailment']), on='time')
df = df.fillna(0)

array = np.array(df)
means = np.mean(array[:,1:].astype(float),axis=0)

for num in range(2,len(array[0])-1):
    for idx,i in enumerate(array):
        startidx = 0
        if i[num] == 0.0:
            for x in range(idx, len(array)):
                if array[x][num] != 0.0:
                    mean = np.mean([array[startidx,num], array[x,num]])

                    if mean == 0:
                        mean = means[num]
            array[idx,num] = mean
        else:
            startidx = idx

for i in range(len(array)-1):
    for j in range(len(array[i])-1):
        if array[i,j]==0:
            array[i,j] = np.mean([array[i-1,j],array[i+1,j]])


per = int(len(array)*0.8)
np.random.seed(1)
#np.random.shuffle(df)

x_train = array[:,1:-1][:per]
y_train = list(array[:,-1])[:per]
x_test = array[:,1:-1][per:]
y_test = list(array[:,-1])[per:]


svc = SVC(kernel="linear", C=0.025).fit(x_train, y_train)
score = cross_val_score(svc, x_train, y_train, cv = KFold(n_splits=5, random_state=1), scoring = "accuracy")

acc_test = svc.score(x_test, y_test)

print('Accuracy development data: ', round(np.mean(score),3), '  min:', round(np.min(score),3), 'max:', round(np.max(score),3))
print('Accuracy test data:        ', round(acc_test,3))

# Output New Model
filename = 'trained_model.sav'
pickle.dump(svc, open(filename, 'wb'))
