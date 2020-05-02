from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from datetime import datetime, timedelta
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from mlflow import log_metric, log_param, log_artifact
from azureml.core import Workspace

class DateTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        None
    
    def fit(self, X, y = None):
        return self

    def transform(self, X, y = None):
        X = X.reset_index()
        X['datetime'] = X['time'].apply(lambda x: datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S'))
        X['year'] = X['datetime'].apply(lambda x: x.year)
        X['month'] = X['datetime'].apply(lambda x: x.month)
        X['day'] = X['datetime'].apply(lambda x: x.day)
        X['hour'] = X['datetime'].apply(lambda x: x.hour)
        X['minute'] = X['datetime'].apply(lambda x: x.minute)
        X['day_of_week'] = X['datetime'].apply(lambda x: x.dayofweek)
        y = X['Total']
        return X[['year', 'month', 'day', 'hour', 'minute', 'day_of_week', 'Total']], y

class Shifter(BaseEstimator, TransformerMixin):
    def __init__(self):
        None
    
    def fit(self, X, y = None):
        return self

    def transform(self, X, y = None, hours = 3):
        X = X[0]
        for i in range(hours):
            colname = f"{i+1}hourback"
            X[colname] = X['Total'].shift(60 * (-i-1))
        X = X.dropna()
        y = X['Total']
        X = X.drop(columns = ['Total'], axis = 1)
        return X, y


if __name__ == '__main__':
    # create the client
    client = InfluxDBClient(host = 'influxus.itu.dk', port = 8086, username = 'lsda', password = 'icanonlyread')
    client.switch_database('orkney')

    # get data
    results = client.query('SELECT * FROM "Generation" where time > now() - 8w ORDER BY time')
    points = results.get_points()
    values = results.raw['series'][0]["values"]
    columns = results.raw['series'][0]["columns"]
    generation_df = pd.DataFrame(values, columns = columns).set_index("time")

    # prepare data
    preparation_pipeline = Pipeline([
        ('date_worker', DateTransformer()),
        ('shifter', Shifter())
    ])

    processed_data = preparation_pipeline.fit_transform(generation_df)

    dim1, dim2 = processed_data[0].shape

    # train data

    lreg_model = Lasso().fit(processed_data[0].iloc[:int(0.8*dim1)], processed_data[1][:int(0.8 * dim1)])
    print(lreg_model.score(processed_data[0].loc[int(0.8 * dim1):], processed_data[1][int(0.8 * dim1):]))

    #predictions = lreg_model.predict()
    log_param("param1", 5)
    log_metric("foo", 1)
    log_metric("foo", 2)
    with open('output.txt', 'w') as f:
        f.write("Hello World!")
    log_artifact("output.txt")

