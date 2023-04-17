# THIS SCRIPT WILL PROVIDE THE DATA FRAME ACCORDING TO SYMBOL AND DATE RANGE
import datetime
import os
import pandas as pd

# var
Path = "D:/WorkSpace/BackTestProject/DataBase/"  # for time being this is fix will figure out later if as be will
# move the database to Sql later on.


class DataBaseUpdate:
    DataFrameSymbolFilter = None
    DataFrameDateRangeFilter = None
    DataFrameDayWiseFilter = None

    @classmethod
    def gui_symbol_and_date_change(cls, symbol_name: str, start_date: datetime, end_date: datetime):
        cls.DataFrameSymbolFilter = symbol_change(symbol_name)
        cls.DataFrameDateRangeFilter = date_range_change(start_date, end_date, cls.DataFrameSymbolFilter)
        cls.DataFrameDayWiseFilter = data_club_day_wise(cls.DataFrameDateRangeFilter)

    @classmethod
    def data_base_updated_frame(cls):
        return cls.DataFrameDayWiseFilter

    @classmethod
    def data_base_symbol_updated_frame(cls):
        return cls.DataFrameSymbolFilter

    @classmethod
    def data_base_range_updated_frame(cls):
        return cls.DataFrameDateRangeFilter


def symbol_change(symbol_name: str) -> pd.DataFrame:
    data_base_file = Path + symbol_name + '.csv'
    df = pd.read_csv(data_base_file)
    df['Date'] = pd.to_datetime(df['Date'])
    print(df)
    return df


def date_range_change(start_date: datetime, end_date: datetime, df: pd.DataFrame) -> pd.DataFrame:
    pass


def data_club_day_wise(dataframe: pd.DataFrame) -> pd.DataFrame:
    pass


