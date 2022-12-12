# -*- coding:utf-8 -*-
import pandas as pd 
import numpy as np 
from statsmodels.tsa.arima_model import ARMA 
import sys 
from dateutil.relativedelta import relativedelta
from copy import deepcopy 
import matplotlib.pyplot as plt 

class arima_model:
    def __init__(self, ts, maxLag=9):
        self.data_ts = ts 
        self.resid_ts = None 
        self.predict_ts = None 
        self.maxLag = maxLag 
        self.p = maxLag 
        self.q = maxLag 
        self.properModel = None 
        self.bic = sys.maxint 

    # 计算最优ARIMA模型, 将相关结果赋值给相应属性
    def get_proper_model(self):
        self._proper_model()
        self.predict_ts = deepcopy(self.properModel.predict())
        self.resid_ts  = deepcopy(self.properModel.resid)

    # 对于给定范围的p,q计算拟合得最好的arima模型，这里是对差分好的数据进行拟合,故差分恒为0
    def _proper_model(self):
        for p in np.arange(self.maxLag):
            for q in np.arange(self.maxLag):
                # print p,q,self.bic
                model = ARMA(self.data_ts, order=(p,q))
                try:
                    results_ARMA = model.fit(disp=1, method='css')
                except:
                    continue 
                bic = results_ARMA.bic 
                # print 'bic',bic,'self.bic:',self.bic 
                if bic < self.bic:
                    self.p = p 
                    self.q = q 
                    self.properModel = results_ARMA 
                    self.bic = bic 
                    self.resid_ts = deepcopy(self.properModel.resid)
                    self.predict_ts = self.properModel.predict()

    # 参数确定模型 
    def certain_model(self, p, q):
        model = ARMA(self.data_ts, order=(p,q))
        try:
            self.properModel = model.fit(disp=1, method='css')
            self.p = p 
            self.q = q 
            self.bic = self.properModel.bic 
            self.predict_ts = self.properModel.predict() 
            self.resid_ts = deepcopy(self.properModel.resid)
        except:
            print 'You can not fit the model with this parameter p,q, '\
                    'please use the get_proper_model method to get the best
                    model'

        # 预测第二日的值
        def forecast_next_day_value(self, type='day'):

