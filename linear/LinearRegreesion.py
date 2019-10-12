import numpy as np


class LinearRegression:

    def __init__(self):
        self.coef_ = None
        self.interception_ = None
        self._theta = None


    def fit(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0]
        X_b = np.hstack([np.ones(len(X_train)), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)

        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]
        
        return self


    def predict(self, X_predict):
        assert X_predict.shape[1] == len(self.coef_)
        # 多元人肉 未完...
        pass

    
    def __repr__(self):
        return "LinearRegression()"
