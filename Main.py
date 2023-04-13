import IndicatorPrediction as Ind_P
import Configuration as conf
import DataManagment as Data_M
import WriteData as Wd

class Initializer:
    def Run():
        conf.Config.LoadConfig() ## LOAD CONFIG
        Data_M.DataManagment.LoadData() ## Filter the Data as per Config
        Ind_P.IndicatorPrediction.Ema_Indicator_Params()
        Ind_P.IndicatorPrediction.Ema_Indicator(10)
        Wd.Writer.WriteShortTradePostion()

if __name__ == '__main__':
    Initializer.Run()