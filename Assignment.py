import math
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

K = [5, 10, 15, 20, 25, 30]
N = [2, 4, 6, 20, 40, 60]

def generateData(featureSize,sampleSize):
    # Generating the data matrix
    samples=np.random.normal(0,scale=2,size=(featureSize,sampleSize))
    # Generating thetaStar
    thetaStar=np.random.normal(loc=0,scale=1,size=(featureSize,1))
    # Generating the noise
    epsilon=np.random.normal(loc=0,scale=np.sqrt(0.1),size=(sampleSize,1))
    # Generating y
    y = np.matmul(samples, thetaStar) + epsilon
    
    return y, samples, thetaStar

def linearRegression(X, Y):
    lin_reg = linear_model.LinearRegression()
    lin_reg.fit(X, Y)
    # X_new = np.random.normal(0,scale=2,size=(3,4))
    # lin_reg.predict(X_new)
    return lin_reg.coef_

def ridgeRegression(X, Y, _lambda):
    ridge_reg = linear_model.Ridge(alpha=_lambda, solver="cholesky")
    ridge_reg.fit(X, Y)
    # X_new = np.random.normal(0,scale=2,size=(3,4))
    # ridge_reg.predict(X_new)
    return ridge_reg.coef_

def l2Distance(originalTheta, computedTheta):
    return math.dist(originalTheta, computedTheta)

K = [5, 10, 15, 20, 25, 30]
N = [2, 4, 6, 20, 40, 60]

for i in range(len(K)):
    for j in range(len(N)):



plt.plot(K, N, 'o')
plt.show()

