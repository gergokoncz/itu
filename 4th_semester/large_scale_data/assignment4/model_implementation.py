from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from datetime import datetime, timedelta


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

    def transform(self, X, y = None, days = 2):
        y = X['Total']
        return X, y


if __name__ == '__main__':
    client = InfluxDBClient(host = 'influxus.itu.dk', port = 8086, username = 'lsda', password = 'icanonlyread')
    client.switch_database('orkney')

    results = client.query('SELECT * FROM "Generation" where time > now() - 4w ORDER BY time')
    points = results.get_points()
    values = results.raw['series'][0]["values"]
    columns = results.raw['series'][0]["columns"]
    generation_df = pd.DataFrame(values, columns = columns).set_index("time")

    date_transformed, target = DateTransformer().fit_transform(generation_df)
    shifted_transformed, target = Shifter().fit_transform(date_transformed, y = target)

    print(shifted_transformed.head(10))
    print(target.head(10))
