import Configuration as conf
from back_test_package import DataManagment as dm

# TEST LOAD DATA FROM CONF

if __name__ == '__main__':
    conf.Config.LoadConfig()
    clss = dm.DataBaseUpdate
    clss.gui_symbol_and_date_change(conf.Config.CONFIG_SYMBOL,conf.Config.CONFIG_START_DATE,conf.Config.CONFIG_END_DATE)
    df = clss.data_base_updated_frame()



