import configparser as cfg
import os
import sys
from pathlib import Path


class Config:
    CONFIG_SYMBOL = None  # Database_string
    CONFIG_START_DATE = None  # Calculation_string
    CONFIG_END_DATE = None  # Calculation_string
    SHORT = None  # Calculation_int
    SPAN = None  # Calculation_boolean
    TYPE = None  # Database_string
    LONG = None  # Database_int

    config_name = 'Config.cfg'

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path, config_name)
    print("CONFIG PATH ---> " + config_path)
    myfile = Path(config_path)

    @staticmethod
    def LoadConfig():
        print("--------==> Config Parse    <==-------")
        if Config.myfile.is_file():
            try:
                config_P = cfg.RawConfigParser()
                config_P.read(Config.config_path)
                Config.CONFIG_SYMBOL = config_P.get('DATASET', 'SYMBOL')
                Config.CONFIG_START_DATE = config_P.get('DATASET', 'StartDate')
                Config.CONFIG_END_DATE = config_P.get('DATASET', 'EndDate')
                Config.TYPE = config_P.get('INDICATOR', 'TYPE')
                Config.SPAN = config_P.getint('INDICATOR', 'SPAN')
                Config.LONG = config_P.get('INDICATOR', 'LONG')
                Config.SHORT = config_P.get('INDICATOR', 'SHORT')


            except:
                print("((ERROR):==>) Something went wrong while loading Configuration.")
        else:
            print("CONFIG FILE NOT FOUND")


# FOR TESTING ----------------->
if __name__ == '__main__':
    Config.LoadConfig()
    print("--- CONFIG VALUE ---")
    print(Config.CONFIG_SYMBOL)
    print(Config.CONFIG_START_DATE)
    print(Config.CONFIG_END_DATE)
    print(Config.SPAN)
    print(Config.LONG)
    print(Config.TYPE)
    print(Config.SHORT)
