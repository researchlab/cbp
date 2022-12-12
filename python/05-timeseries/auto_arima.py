# reference: https://blog.51cto.com/u_15255081/5477884
import datetime 
import time 
import tsod  #tsod可以完成时序数据的异常检测
import pandas as pd
import pmdarima as pm 
import matplotlib.pyplot as plt 
from statsmodels.tsa.stattools import adfuller 
from sklearn.metrics import mean_absolute_error

class AutoARIMA(object):
    def __init__(self):
        air_passenger = pd.read_csv('./data/AirPassengers.csv')
        air_passenger['Month'] = pd.to_datetime(air_passenger['Month']) # datetime格式化
        # 设置Month列为索引列
        air_passenger.set_index('Month',inplace=True)
        self.ts = air_passenger['Passengers']
        # 取n_periods 为测试集
        self.n_periods = 5 

        # 把数据划分为训练集和测试集，就可以拿训练集来训练，拿测试集来评估训练的好坏，
        # 接下来我们来结合auto_arima的超参数进行一些不同的建模试尝试
        self.train_ts = self.ts[0:-self.n_periods]
        self.test_ts = self.ts[-self.n_periods:]

    def show(self):
        # 新建12*8 画布
        fig = plt.figure(figsize=(12,8))
        # 原时序图
        self.ts.plot(label='origin ts')
        # 横坐标逆时针倾斜45度
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
    def predict(self, model):
        start_time = time.time()
        print("best model:", model)
        y_pred = model.predict(self.n_periods) # 预测未来n_periods 期
        mae = mean_absolute_error(self.test_ts.values, y_pred)
        print("mean_absolute_error:", mae)
        print("cost time:", time.time() - start_time)

    # 1.首先是不带任何超参的模型，只有要拟合的时序train_ts，此时所有的超参都是默认设置。
    def default(self):
        return pm.auto_arima(self.train_ts)
    # 2.原auto_arima默认是stepwies = True，我们加入一个stepwies = False的超参数看一看效果
    def with_step_wise(self):
        return pm.auto_arima(self.train_ts, stepwise=False)
    # 3.从原时序图可以明显观察到时序是周期性的，可以加入season参数
    def with_season(self):
        return pm.auto_arima(self.train_ts, seasonal=True, seasonal_test='ocsb')
    # 4.从原时序图我们还看到了乘客人数有整体上升的趋势，于是可以加入trend超参
    def with_trend(self):
        return pm.auto_arima(self.train_ts, trend='c')
    # 5.
    def with_trend_season(self):
        return pm.auto_arima(self.train_ts, seasonal=True,
                             seasonal_test='ocsb', trend='c')
    # 6.加入季节因子
    def with_m_trend_season(self):
        return pm.auto_arima(self.train_ts, seasonal=True,
                             seasonal_test='ocsb', trend='c', m=12)
    # 7.all in one 
    def all(self):
        return pm.auto_arima(self.train_ts,
                             start_p=1,d=None,start_q=1,
                             max_p=5,max_d=2,max_q=5,
                             start_P=1,D=None,start_Q=1,
                             max_P=2,max_D=1,max_Q=2,
                             max_order=None,
                             test='kpss', #当非平稳且d=None才会进⾏检验
                             m=12,
                             seasonal=True,
                             seasonal_test='ocsb', # 单位根检测方法
                             trend='c', # c表示常数项趋势
                             information_criterion='aic', #赤池信息准则
                             trace=False,
                             with_intercept='auto',
                             error_action='ignore',
                             suppress_warnings=True,
                             maxiter=100,
                             stepwise=False)
if __name__ == "__main__":
    aa = AutoARIMA()
    # show() 会阻塞，所以需要show同时需要执行之后的代码，需要多线程
    #aa.show()
    #aa.predict(aa.default())
    '''output
    best model:  ARIMA(4,1,3)(0,0,0)[0]
    mean_absolute_error: 53.99605698603659
    cost time: 0.007561206817626953
    '''
    #aa.predict(aa.with_step_wise())
    '''output
    best model:  ARIMA(0,1,4)(0,0,0)[1] intercept
    mean_absolute_error: 76.59424066739764
    cost time: 0.01018977165222168
    在设置stepwise=False之后，最佳拟合的ARIMA变了有了季节因子的SARIMA，耗时更少，平均绝对误差变大了
    '''
    #aa.predict(aa.with_season())
    '''output
    best model:  ARIMA(4,1,3)(0,0,0)[0]
    mean_absolute_error: 53.99605698603659
    cost time: 0.008091926574707031
    虽然设置了season=True 和 season_test='ocsb',
    但是拟合的模型季节阶还是0，明显没有寻出季节性参数
    '''
    #aa.predict(aa.with_trend())
    '''output
    best model:  ARIMA(1,1,1)(0,0,0)[0]
    mean_absolute_error: 156.21292981496845
    cost time: 0.009000062942504883
    '''
    #aa.predict(aa.with_trend_season())
    '''output
    best model:  ARIMA(1,1,1)(0,0,0)[0] intercept
    mean_absolute_error: 156.21292981496845
    cost time: 0.008028268814086914
    '''
    #aa.predict(aa.with_m_trend_season())
    '''output
    best model:  ARIMA(1,1,0)(0,1,0)[12] intercept
    mean_absolute_error: 32.803721314597546
    cost time: 0.008875846862792969
    设置m参数之后，mae 明显降下来了，看来m参数是一个重要的参数
    '''
    aa.predict(aa.all())
    '''output
    best model:  ARIMA(2,1,3)(1,1,2)[12]
    mean_absolute_error: 14.785365629681916
    cost time: 0.011035680770874023
    可以看到设置了诸多调教参数后，效果最好，但是也增加了一个数量级的耗时
    '''
