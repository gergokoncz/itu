import pickle
import pandas as pd
import numpy as np
from influxdb import InfluxDBClient

client = InfluxDBClient(host='influxus.itu.dk', port=8086, username='lsda', password='icanonlyread')
client.switch_database('orkney')

df = pd.DataFrame()

results = client.query('SELECT mean(Total) FROM "Demand" WHERE time > now() - 1d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = pd.concat([df, pd.DataFrame(values,columns=['time', 'demand'])], axis=1)

results = client.query('SELECT mean("M/S") FROM "Wind" WHERE time > now() - 1d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = df.merge(pd.DataFrame(values, columns=['time', 'wind']), on='time')

results = client.query('SELECT mean("u") FROM "Wind" WHERE time > now() - 1d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = df.merge(pd.DataFrame(values, columns=['time', 'u wind']), on='time')

results = client.query('SELECT mean("v") FROM "Wind" WHERE time > now() - 1d GROUP BY time(1h)') # Query written in InfluxQL
values = results.raw["series"][0]["values"]
df = df.merge(pd.DataFrame(values, columns=['time', 'v wind']), on='time')

df = df.fillna(0)
array = np.array(df)

means = np.mean(array[:,1:].astype(float),axis=0)

for num in range(2,len(array[0])):
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

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i,j]==0:
            array[i,j] = np.mean([array[i-1,j],array[i+1,j]])

x = array[:,1:]

svc = pickle.load(open('trained_model.sav', 'rb'))

pred = pd.DataFrame(svc.predict(x))
pred.to_csv('predicted_curtailment.csv', index=False)
