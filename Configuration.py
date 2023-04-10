import configparser as cfg
import os
import sys

class Config:
    CONFIG_SYMBOL = None #Database_string
    CONFIG_START_DATE = None #Calculation_string
    CONFIG_END_DATE = None #Calculation_string
    CONFIG_RANGE = None #Calculation_int
    CONFIG_IS_RANGE_ENABLE = None #Calculation_boolean
    
    config_name = 'Resources\Config.cfg'

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path, config_name)
    print("CONFIG PATH ---> "+ config_path)
    
    def LoadConfig():
        config_P = cfg.RawConfigParser()
        config_P.read(Config.config_path) 
        Config.CONFIG_SYMBOL = config_P.get('Database','SYMBOL') 
        Config.CONFIG_IS_RANGE_ENABLE = config_P.getboolean('Calculation','IS_RANGE_ENABLE')
        Config.CONFIG_START_DATE = config_P.get('Calculation','StartDate')
        Config.CONFIG_END_DATE = config_P.get('Calculation','EndDate')
        Config.CONFIG_RANGE = config_P.getint('Calculation','Range')
        
#FOR TESTING ----------------->
if __name__ == '__main__':
    Config.LoadConfig()
    print("--- CONFIG VALUE ---")
    print(Config.CONFIG_SYMBOL)
    print(Config.CONFIG_START_DATE)
    print(Config.CONFIG_END_DATE)
    print(Config.CONFIG_RANGE)
    print(Config.CONFIG_IS_RANGE_ENABLE)