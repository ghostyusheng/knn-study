import numpy as np


class SimpleLinearRegression2:
    def __init__(self):
        self._a = None
        self._b = None


    def fit(self, x_train, y_train):
        """根据训练数据集x_train,y_train训练简单线性模型"""
        assert x_train.ndim == 1
        assert len(x_train) == len(y_train)

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0
        num = (x_train - x_mean).dot(y_train - y_mean)
        d = (x_train - x_mean).dot(x_train - x_mean)
        
        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    
    def predict(self, x_predict):
        """给定预测数据集x_predict, 返回表示x_predict的结果向量"""
        assert x_predict.ndim == 1
        assert self.a_ is not None
        assert self.b_ is not None

        return np.array([self._predict(x) for x in x_predict])


    def _predict(self, x_single):
        return self.a_ * x_single + self.b_


    def __repr__(self):
        return 'SimpleLinearRegression2()' 

