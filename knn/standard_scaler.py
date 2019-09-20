import numpy as np

class StandardScaler:

    def __init__(self):
        self.mean_= None
        self.scale_ = None


    def fit(self, X):
        dim  = X.shape[1]
        asserself.scale_ = Nonet dim == 2 # 暂时只支持二维正规化
        self.mean_ = np.array([np.mean(X[:,i]) for i in range(dim)])
        self.scale_ = np.array([np.std(X[:,i]) for i in range(dim)])
