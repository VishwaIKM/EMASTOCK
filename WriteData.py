import IndicatorPrediction as Ind_P
import DataManagment as Data_M
import numpy as np 
import Configuration as Conf
import matplotlib.pyplot as plt
import pandas as pd

class Writer:
    DATA_WITH_POSTION = None
    def WriteShortTradePostion():
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Signal'] = 0.0
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Signal'] = np.where(Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Close']>Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['EMA'+str(Conf.Config.CONFIG_EMA)],1.0,0.0)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Position'] = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Signal'].diff()
        finalData = np.where(Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Position'] != 0.0)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE= Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.loc[finalData]
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.reset_index()
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.drop(['Signal'], axis=1)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.drop(['index'], axis=1)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.drop(['Open'], axis=1)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.drop(['High'], axis=1)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.drop(['Low'], axis=1)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Symbol'] = str(Conf.Config.CONFIG_SYMBOL)

        
        #print(Ind_P.IndicatorPrediction.DATA_CLUB_VALUE)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.to_csv('FinalDateForshorSelling.csv',index = False)
        df1 = pd.read_csv('FinalDateForshorSelling.csv', skiprows=[1])
        #print(df1)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['ExitPrice'] = df1['Close']
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Trade'] = 'Short'
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['ExitTime'] = '15:30:00'
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['EntryTime'] = '09:15:00'
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Profit'] = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['Close'] - Ind_P.IndicatorPrediction.DATA_CLUB_VALUE['ExitPrice'] 
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE = Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.drop(['Position'], axis=1)
        #print(Ind_P.IndicatorPrediction.DATA_CLUB_VALUE) 
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.rename(columns = {'Close': 'EntryPrice'},inplace=True)
        Ind_P.IndicatorPrediction.DATA_CLUB_VALUE.to_csv('FinalDateForshorSelling.csv',index = False)

if __name__ == '__main__':
    Conf.Config.LoadConfig()
    Data_M.DataManagment.LoadData()
    Ind_P.IndicatorPrediction.Ema_Indicator_Params()
    Ind_P.IndicatorPrediction.Ema_Indicator(10)
    Writer.WriteShortTradePostion()