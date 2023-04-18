import pandas as pd


class FileWriter:
    def __int__(self, df: pd.DataFrame) -> None:
        self.df = df

    def write_data(self, name: str) -> bool:
        if self.df.to_csv(name, index=False):
            return True
