import Configuration as conf
import DataManagment as Data_M
class Initializer:
    def Run():
        conf.Config.LoadConfig() ## LOAD CONFIG
        Data_M.DataManagment.LoadData() ## Filter the Data as per Config


if __name__ == '__main__':
    Initializer.Run()