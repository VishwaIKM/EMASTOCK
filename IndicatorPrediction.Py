import DataManagment as Data_M
import Configuration as Conf

class IndicatorPrediction:
    
    def Ema_Indicator_Params():
        #Value Find on The Basic of Config
        pass

    def Ema_Indicator(Indicator_Span):
        #writeInFile


        #DrawTheGraph
        pass


#FOR TESTING ----------------->
if __name__ == '__main__':
    Conf.Config.LoadConfig()
    Data_M.DataManagment.LoadData()
    IndicatorPrediction.Ema_Indicator_Params()
    IndicatorPrediction.Ema_Indicator()