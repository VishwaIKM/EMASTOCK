# THIS SCRIPT WILL PROVIDE THE DATA FRAME ACCORDING TO SYMBOL AND DATE RANGE
from datetime import datetime
import pandas as pd

# var
Path = "C:/Users/vishw/OneDrive/Documents/WORKSPACE/back_test_project/DataBase/"  # for time being this is fix will


# figure out later if as be will
# move the database to Sql later on.


class DataBaseUpdate:
    DataFrameSymbolFilter: pd.DataFrame = None
    DataFrameDateRangeFilter: pd.DataFrame = None
    DataFrameDayWiseFilter: pd.DataFrame = None

    @classmethod
    def gui_symbol_and_date_change(cls, symbol_name: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        # print(f"SD:{start_date} and ED:{end_date}")
        cls.DataFrameSymbolFilter = symbol_change(symbol_name)
        cls.DataFrameDateRangeFilter = date_range_change(start_date, end_date, cls.DataFrameSymbolFilter)
        cls.DataFrameDayWiseFilter = data_club_day_wise(cls.DataFrameDateRangeFilter)
        return cls.DataFrameDayWiseFilter

    """Below Class method for future ref if additional data manipulation required  """

    @classmethod
    def data_base_updated_frame(cls) -> pd.DataFrame:
        return cls.DataFrameDayWiseFilter

    @classmethod
    def data_base_symbol_updated_frame(cls) -> pd.DataFrame:
        return cls.DataFrameSymbolFilter

    @classmethod
    def data_base_range_updated_frame(cls) -> pd.DataFrame:
        return cls.DataFrameDateRangeFilter


def symbol_change(symbol_name: str) -> pd.DataFrame:
    data_base_file = Path + symbol_name + '.csv'
    df = pd.read_csv(data_base_file)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def date_range_change(start_date: datetime, end_date: datetime, df: pd.DataFrame) -> pd.DataFrame:
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    return df


def data_club_day_wise(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['Date']).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    return df
