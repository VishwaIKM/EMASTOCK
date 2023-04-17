# THIS SCRIPT WILL PROVIDE THE INDICATOR CALCULATION
import pandas as pd
from abc import ABC, abstractmethod


class BaseIndicator(ABC):
    def __int__(self, df: pd.DataFrame, span: int, price: str) -> None:
        self.df = df
        self.span = span
        self.price = price

    def start_indicator_calculation(self) -> None:
        self.add_indicator()
        self.base_graph(self.price)

    def base_graph(self, param: str) -> pd.Series:
        return self.df[param]

    @abstractmethod
    def add_indicator(self) -> pd.DataFrame:
        pass


class ExponentialMovingAverage(BaseIndicator):
    def add_indicator(self) -> pd.DataFrame:
        self.df['EMA ' + str(self.span)] = self.df[self.price].ewm(span=self.span, adjust=False).mean()
        return self.df


class ExponentialMovingLongShortAverage(BaseIndicator):

    def __int__(self, df: pd.DataFrame, short_span: int, price: str,long_span: int) -> None:
        super().__int__(df, short_span, price)
        self.long_span = long_span

    def ema_long_short_add(self) -> pd.DataFrame:
        pass

    def add_indicator(self) -> pd.DataFrame:
        self.df['EMA ' + str(self.span)] = self.df[self.price].ewm(span=self.span, adjust=False).mean()
        return self.df
