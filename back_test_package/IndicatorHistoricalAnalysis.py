# THIS SCRIPT WILL PROVIDE THE GRAPH AND BUY SELL VALUE
import numpy as np
import pandas as pd
from abc import ABCMeta, abstractmethod, ABC


class BaseHistoricalAnalysis(object):
    __metaclass__ = ABCMeta

    def __init__(self, df: pd.DataFrame, span: int, price: str):
        self.df = df
        self.span = span
        self.price = price

    @abstractmethod
    def buy_sell_analysis(self) -> pd.DataFrame:
        pass


class ExponentialMovingAverage(BaseHistoricalAnalysis):

    def buy_sell_analysis(self) -> pd.DataFrame:
        df = self.df
        df['Signal'] = np.where(df[self.price] > df['EMA ' + str(self.span)], 1.0, 0.0)
        df['Position'] = df['Signal'].diff()
        df['Transaction'] = np.where(df['Position'] > 0.0, 'SELL', 'BUY')
        df = df.reset_index()

        df = df.iloc[np.where(df['Position'] != 0.0)]
        df = df.reset_index()

        sf = df.tail(-1)
        sf = sf.reset_index()

        df['Exit Price'] = sf[self.price]
        df = df.reset_index()

        # remove reset old index
        df = df.drop(['index'], axis=1)
        df = df.drop(['level_0'], axis=1)
        df = df.drop(['Signal'], axis=1)
        df = df.drop(['Position'], axis=1)

        df['Profit'] = np.where(df['Transaction'] == 'BUY', df['Exit Price'] - df[self.price], df[self.price] - df['Exit Price'])

        self.df = df  # just to save the df in instance for other function
        return self.df


class ExponentialMovingLongShortAverage(BaseHistoricalAnalysis):

    def __init__(self,df: pd.DataFrame, short_span: int, price: str,long_span: int):
        super().__init__(df,short_span,price)
        self.long_span = long_span

    def buy_sell_analysis(self) -> pd.DataFrame:
        df = self.df
        df['Signal'] = np.where(df['EMA ' + str(self.long_span)] > df['EMA ' + str(self.span)], 1.0, 0.0)
        df['Position'] = df['Signal'].diff()
        df['Transaction'] = np.where(df['Position'] > 0.0, 'SELL', 'BUY')
        df = df.reset_index()

        df = df.iloc[np.where(df['Position'] != 0.0)]
        df = df.reset_index()

        sf = df.tail(-1)
        sf = sf.reset_index()

        df['Exit Price'] = sf[self.price]
        df = df.reset_index()

        df = df.drop(['index'], axis=1)
        df = df.drop(['level_0'], axis=1)
        df = df.drop(['Signal'], axis=1)
        df = df.drop(['Position'], axis=1)

        df['Profit'] = np.where(df['Transaction'] == 'BUY', df['Exit Price'] - df[self.price],
                                df[self.price] - df['Exit Price'])

        self.df = df  # just to save the df in instance for other function
        return self.df

