# THIS SCRIPT WILL PROVIDE THE INDICATOR CALCULATION
import pandas as pd
from abc import ABCMeta, abstractmethod


class BaseIndicator(object):
    __metaclass__ = ABCMeta

    def __init__(self, df: pd.DataFrame, span: int, price: str) -> None:
        self.df = df
        self.span = span
        self.price = price

    def base_graph(self, param: str) -> pd.Series:
        return self.df[param]

    @abstractmethod
    def add_indicator(self) -> pd.DataFrame:
        pass


class ExponentialMovingAverage(BaseIndicator): # metaclass=ABCMeta
    def add_indicator(self) -> pd.DataFrame:
        self.df['EMA ' + str(self.span)] = self.df[self.price].ewm(span=self.span, adjust=False).mean()
        return self.df


class ExponentialMovingLongShortAverage(BaseIndicator): # metaclass=ABCMeta
    def __init__(self, df: pd.DataFrame, short_span: int, price: str, long_span: int) -> None:
        super().__init__(df, short_span, price)
        self.long_span = long_span

    def add_indicator(self) -> pd.DataFrame:
        self.df['EMA ' + str(self.span)] = self.df[self.price].ewm(span=self.span, adjust=False).mean()
        self.df['EMA ' + str(self.long_span)] = self.df[self.price].ewm(span=self.long_span, adjust=False).mean()
        return self.df
