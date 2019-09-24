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


    def tranform(self, X)
        assert X.ndim == 2
        assert X.shape[1] == len(self.mean_)
        resX = np.empty(shape=X.shape, dtype=float)
        for col in range(X.shape[1])
            resX[:,col] = (X[:,col] - self.mean_[col]) / self.scale_[col]
        return resX
