from math import sqrt
import numpy as np

# MSE
def mean_squared_error(y_true, y_predict):
    assert len(y_true) == len(y_predict)
    return np.sum((y_true - y_predict) ** 2) / len(y_true)

#RMSE
def root_mean_squared_error(y_true, y_predict):
    return sqrt(mean_squared_error(y_true, y_predict))


#MAE
def mean_absolute_error(y_true, y_predict):
    assert len(y_true) == len(y_predict)
    return np.sum(np.absolute(y_true - y_predict)) / len(y_true)
