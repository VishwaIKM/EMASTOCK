import Configuration as conf
from back_test_package import DataManagment as dm
from back_test_package.Indicators import ExponentialMovingAverage as EMA
from back_test_package.Indicators import ExponentialMovingLongShortAverage as EMA2
from back_test_package.IndicatorHistoricalAnalysis import ExponentialMovingAverage as EM
from back_test_package.IndicatorHistoricalAnalysis import ExponentialMovingLongShortAverage as EM2

from datetime import datetime

# TEST LOAD DATA FROM CONF

if __name__ == '__main__':
    conf.Config.LoadConfig()
    clss = dm.DataBaseUpdate()
    dt = datetime.strptime(conf.Config.CONFIG_START_DATE, '%d-%m-%Y')
    bt = datetime.strptime(conf.Config.CONFIG_END_DATE, '%d-%m-%Y')
    val = clss.gui_symbol_and_date_change(conf.Config.CONFIG_SYMBOL, dt, bt)
    # print(val)
    # inik = EMA(val,10,'Close')
    # p = inik.add_indicator()
    # print(p)

    ik = EMA2(val, 10, 'Close', 15)
    val = ik.add_indicator()
    print(val)
    # print(ik.add_indicator())
    # print(ik.base_graph('EMA 15'))
    # test = EM(p,10,'Close')

    # print(test.buy_sell_analysis())

    test2 = EM2(val, 10, 'Close', 15)
    print(test2.buy_sell_analysis())
