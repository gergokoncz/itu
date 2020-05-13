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
        return X.set_index('datetime')

class Shifter(BaseEstimator, TransformerMixin):
    def __init__(self):
        None
    
    def fit(self, X, y = None, days = 3):
        return self

    def fit_transform(self, X, y = None, days = 3):
        for i in range(days):
            colname = f"{i+1}dayback"
            X[colname] = X['Total'].shift(i+1, freq = 'D')
        X = X.dropna()
        y = X['Total']
        #X = X.drop(columns = ['Total'], axis = 1)
        return X, y
