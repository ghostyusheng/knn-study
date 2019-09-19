import math
import numpy as np
from collections import Counter

def accuracy_score(y_true, y_predict):
    """计算y_true 和 y_predict之间的准确率"""
    """y_true真值，y_predict预测值"""
    return sum(y_true == y_predict) / len(y_true)


def train_test_split(X, y, test_ratio=0.2):
    SAMPLE_SIZE = X.shape[0]
    test_size = int(SAMPLE_SIZE * test_ratio)
    shuffle_indexes = np.random.permutation(SAMPLE_SIZE)
    X_test = X[shuffle_indexes[:test_size]]
    y_test = y[shuffle_indexes[:test_size]]
    X_train = X[shuffle_indexes[test_size:]]
    y_train = y[shuffle_indexes[test_size:]]
    return X_train, X_test, y_train, y_test


def kNN_classify(k, X_train, y_train, x):
    assert 1 <= k <= X_train.shape[0]
    assert X_train.shape[0] == y_train.shape[0]
    assert X_train.shape[1] == x.shape[0]

    distances = [math.sqrt(np.sum((x_train - x)**2)) for x_train in X_train]
    nearest = np.argsort(distances)

    topK_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(topK_y)
    return votes.most_common(1)[0][0]


class KNNClassifier:
    def __init__(self, k):
        assert k >= 1
        self.k = k
        self._X_train = None
        self._y_train = None


    def fit(self, X_train, y_train):
        """
        根据训练数据集X_train和y_train训练KNN分类器
        """
        assert X_train.shape[0] == y_train.shape[0]
        assert self.k <= X_train.shape[0]

        self._X_train = X_train
        self._y_train = y_train
        return self


    def predict(self, X_predict):
        """根据预测数据，返回表示X_predict的结果向量"""
        assert self._X_train is not None and self._y_train is not None
        assert X_predict.shape[1] == self._X_train.shape[1]

        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    
    def _predict(self, x):
        assert x.shape[0] == self._X_train.shape[1]

        distances = [math.sqrt(np.sum((x_train - x)**2)) for x_train in self._X_train]
        nearest = np.argsort(distances)

        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    
    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)


    def __repr__(self):
        return "KNN(k=%d)" % self.k
