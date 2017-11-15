from datetime import datetime
import pandas as pd
from pandas.io.json import json_normalize


def to_dataframe(data):
    """ """
    return json_normalize(data)


def value_counts(df):
    """ """
    return df.value_counts()


def most_common(df, topn=20):
    """ """
    return df.value_counts()[:topn]


def plot_most_common(df, column, topn=20):
    """ """
    return df[column].value_counts()[:topn].plot(kind='barh')


def plot_time_series(d):
    """ """
    df = pd.DataFrame(d)
    df['first_seen'] = pd.to_datetime(df['first_seen'], unit="ns")
    df['timestamp'] = df.first_seen.map(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
    df['hits'] = 1

    ts = df.groupby('timestamp').sum()
    del ts['metadata.tor']
    ts.index = pd.to_datetime(ts.index)
    ts = ts.resample('D').sum()
    ts.counts.fillna(0, inplace=True)
    return ts.plot()
