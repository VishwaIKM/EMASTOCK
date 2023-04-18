import Configuration as conf
from back_test_package import DataManagment as dm
from datetime import datetime
# TEST LOAD DATA FROM CONF

if __name__ == '__main__':
    conf.Config.LoadConfig()
    clss = dm.DataBaseUpdate()
    dt = datetime.strptime(conf.Config.CONFIG_START_DATE, '%d-%m-%Y')
    bt = datetime.strptime(conf.Config.CONFIG_END_DATE, '%d-%m-%Y')
    val = clss.gui_symbol_and_date_change(conf.Config.CONFIG_SYMBOL, dt, bt)
    print(val)
    df = clss.data_base_updated_frame()



