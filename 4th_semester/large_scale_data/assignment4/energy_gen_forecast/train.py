from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import mytransformers
from sklearn.model_selection import TimeSeriesSplit

import os, warnings, sys

import logging
logging.basicConfig(level = logging.WARN)
logger = logging.getLogger(__name__)

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def get_data(weeks = 8):
    client = InfluxDBClient(host = 'influxus.itu.dk', port = 8086, username = 'lsda', password = 'icanonlyread')
    client.switch_database('orkney')

    results = client.query('SELECT * FROM "Generation" where time > now() - {}w ORDER BY time'.format(str(weeks)))
    points = results.get_points()
    values = results.raw['series'][0]["values"]
    columns = results.raw['series'][0]["columns"]
    return pd.DataFrame(values, columns = columns).set_index("time")


if __name__ == '__main__':
    # handle params
    weeks = int(sys.argv[1] if len(sys.argv) > 1 else 8)
    hours = int(sys.argv[2] if len(sys.argv) > 2 else 3)
    alpha = float(sys.argv[3] if len(sys.argv) > 3 else 0.5)

    generation_df = get_data(weeks)

    # prepare data
    pre_pipeline = Pipeline([
        ('date_worker', mytransformers.DateTransformer()),
        ('shifter', mytransformers.Shifter())
    ])

    processed_data = pre_pipeline.fit_transform(generation_df, shifter__hours = hours)
    features = processed_data[0]
    labels = processed_data[1]

    # start mlflow run
    with mlflow.start_run():
        # cross validation
        tscv = TimeSeriesSplit(5)
        for train_index, test_index in tscv.split(labels):
            X_train, X_test = features.iloc[train_index], features.iloc[test_index]
            y_train, y_test = labels[train_index], labels[test_index]
            model = Lasso(alpha).fit(X_train, y_train)
            preds = model.predict(X_test)

            rmse, mae, r2 = eval_metrics(y_test, preds)

            mlflow.log_param("alpha", alpha)
            mlflow.log_param("weeks", weeks)
            mlflow.log_param("hours", hours)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
