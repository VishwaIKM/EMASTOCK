import DataManagment as Data_M
import Configuration as Conf
import matplotlib.pyplot as plt
import pandas as pd
class IndicatorPrediction:
    DATA_CLUB_VALUE = None
    DATA_FRAME_AFTER_CLUB =None
    def Ema_Indicator_Params():
        #Value Find on The Basic of Config
        if(str(Conf.Config.CONFIG_EMA_TYPE) == "MM"):
            pass
        elif(str(Conf.Config.CONFIG_EMA_TYPE) == "HH"):
            pass
        elif(str(Conf.Config.CONFIG_EMA_TYPE) == "DD"):
            #data club will be done on DateWis
            pass
                

    def Ema_Indicator(Indicator_Span):
        #writeInFile
        if(str(Conf.Config.CONFIG_EMA_TYPE) == "DD"):
            dicdate = None
            Data_M.DataManagment.Filter_Data_Frame =Data_M.DataManagment.Filter_Data_Frame.reset_index()
            Data_M.DataManagment.Filter_Data_Frame = Data_M.DataManagment.Filter_Data_Frame.drop(['index'], axis=1)
            #print(Data_M.DataManagment.Filter_Data_Frame)
            gp =  Data_M.DataManagment.Filter_Data_Frame.groupby(['Date']).agg({'Open':'first','High':'max','Low':'min','Close':'last'})
            gp = gp.reset_index()
            ema = gp['Close'].ewm(span=int(Conf.Config.CONFIG_EMA),adjust=False).mean()
            #print(ema)
            gp['EMA'+str(Conf.Config.CONFIG_EMA)] = ema
            #print(gp)
            gp.to_csv('RAWDATA.csv')
            # Comparison plot b/w stock values & EMA
            plt.plot(gp['Close'], label="Stock Values")
            plt.plot(ema, label="EMA Values")
            plt.xlabel("Days")
            plt.ylabel("Price")
            plt.legend()
            plt.show()
            IndicatorPrediction.DATA_CLUB_VALUE = gp
            #print(IndicatorPrediction.DATA_CLUB_VALUE)


#FOR TESTING ----------------->
if __name__ == '__main__':
    Conf.Config.LoadConfig()
    Data_M.DataManagment.LoadData()
    IndicatorPrediction.Ema_Indicator_Params()
    IndicatorPrediction.Ema_Indicator(10)