#

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error

class GDLinearRegression:
    def __init__(self, learning_rate, epoch):
        self.learning_rate, self.iterations = learning_rate, epoch
 
    def fit(self, X, y):
        c = 0
        m = 5
        n = X.shape[0]
        for _ in range(self.iterations):
            b_gradient = -2 * np.sum(y - m*X + c) / n
            m_gradient = -2 * np.sum(X*(y - (m*X + c))) / n
            c = c + (self.learning_rate * b_gradient)
            m = m - (self.learning_rate * m_gradient)
        self.m, self.c = m, c
 
    def predict(self, X):
        return self.m*X + self.c

#dataset
np.random.seed(42)
X = np.array(sorted(list(range(5))*20)) + np.random.normal(size = 100, scale = 0.5)
y = np.array(sorted(list(range(5))*20)) + np.random.normal(size = 100, scale = 0.3)


Clf_2 = GDLinearRegression(learning_rate = 0.2, epoch = 1000)
Clf_2.fit(X, y)
y_pred = Clf_2.predict(X)
mse_2 = mean_squared_error(y, y_pred)
plt.style.use('fivethirtyeight')
plt.scatter(X, y, color='black')
plt.plot(X, y_pred)
plt.gca().set_title("Linear Regression Model 2")
plt.show()

print('RMSE = ', round(sqrt(mse_2), 2))


