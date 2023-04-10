# TIME GAP FIND
#
import Configuration as Conf
import pandas as pd
from dateutil import parser
from datetime import datetime, timedelta


class DataManagment:

    TIME_GAP_BETWEEN_DATA = None  # TICK SIZE
    Filter_Data_Frame = None

    def LoadData():
        # need to define range
        df = pd.read_csv("Data/"+str(Conf.Config.CONFIG_SYMBOL)+"-I.csv")
        DataManagment.TIME_GAP_BETWEEN_DATA = (df.iloc[1, 2]-df.iloc[0, 2])/100
        #print(DataManagment.TIME_GAP_BETWEEN_DATA)
        # df.info()
        df['Date'] = pd.to_datetime(df['Date'])
        # df.info()
        if (Conf.Config.CONFIG_IS_RANGE_ENABLE):
          dd = (datetime.now() - timedelta(days=int(Conf.Config.CONFIG_RANGE))
                ).strftime('%d-%m-%Y')
          split = dd.split('-')
          YY = int(split[2])
          MM = int(split[1])
          DD = int(split[0])
          df = df[(df['Date'] >= datetime(YY, MM, DD))]
        else:
            split = str(Conf.Config.CONFIG_START_DATE).split('-')
            YY = int(split[2])
            MM = int(split[1])
            DD = int(split[0])
            split = str(Conf.Config.CONFIG_END_DATE).split('-')
            YY1 = int(split[2])
            MM1 = int(split[1])
            DD1 = int(split[0])
            df = df[(df['Date'] <= datetime(YY1, MM1, DD1))
                    & (df['Date'] >= datetime(YY, MM, DD))]
        print("--------==> DATA BASE UPDATED <==-------")
        DataManagment.Filter_Data_Frame = df

        # print(df)
        # for index,row in df.iterrows():
        #     print(row['Date'], row['Close'])


if __name__ == '__main__':
    Conf.Config.LoadConfig()
    DataManagment.LoadData()
    print("Data Frame: --\n",DataManagment.Filter_Data_Frame)
    print("Time Gap :",DataManagment.TIME_GAP_BETWEEN_DATA)
