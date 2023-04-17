# THIS SCRIPT WILL PROVIDE THE INDICATOR CALCULATION
import pandas as pd


class ExponentialMovingAverage:

    def __int__(self, data_frame: pd.DataFrame, span: int, price: str):
        self.data_frame = data_frame
        self.span = span
        self.price = price

    def ema_data_add(self) -> pd.DataFrame:
        pass


class ExponentialMovingLongShortAverage:

    def __int__(self, data_frame: pd.DataFrame, short_span: int, long_span: int, price: str):
        self.data_frame = data_frame
        self.short_span = short_span
        self.long_span = long_span
        self.price = price

    def ema_long_short_add(self) -> pd.DataFrame:
        pass
