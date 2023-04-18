# THIS SCRIPT WILL PROVIDE THE DATA FRAME ACCORDING TO SYMBOL AND DATE RANGE
from datetime import datetime
import pandas as pd
import os
import sys

# var
_Path = os.path.dirname(os.path.dirname(__file__)) + "\\DataBase\\"  # for time being this is fix will


# figure out later if as be will
# move the database to Sql later on.


class DataBaseUpdate:
    _DataFrameSymbolFilter: pd.DataFrame = None
    _DataFrameDateRangeFilter: pd.DataFrame = None
    _DataFrameDayWiseFilter: pd.DataFrame = None

    def __inti__(self):
        pass

    def gui_symbol_and_date_change(self, symbol_name: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        # print(f"SD:{start_date} and ED:{end_date}")
        print(_Path)
        self._DataFrameSymbolFilter = _symbol_change(symbol_name)
        self._DataFrameDateRangeFilter = _date_range_change(start_date, end_date, self._DataFrameSymbolFilter)
        self._DataFrameDayWiseFilter = _data_club_day_wise(self._DataFrameDateRangeFilter)
        return self._DataFrameDayWiseFilter

    """Below Class method for future ref if additional data manipulation required  """

    def data_base_updated_frame(self) -> pd.DataFrame:
        return self._DataFrameDayWiseFilter

    def data_base_symbol_updated_frame(self) -> pd.DataFrame:
        return self._DataFrameSymbolFilter

    def data_base_range_updated_frame(self) -> pd.DataFrame:
        return self._DataFrameDateRangeFilter


def _symbol_change(symbol_name: str) -> pd.DataFrame:
    data_base_file = _Path + symbol_name + '.csv'
    df = pd.read_csv(data_base_file)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def _date_range_change(start_date: datetime, end_date: datetime, df: pd.DataFrame) -> pd.DataFrame:
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    return df


def _data_club_day_wise(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['Date']).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    return df
