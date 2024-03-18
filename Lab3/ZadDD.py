import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import scipy.stats as stats
from scipy.stats import multivariate_normal
import seaborn as sns
mean1 = np.array([0, 0])
cov1 = np.array([[4.40, -2.75], [-2.75,  5.50]])
X1_rv=multivariate_normal(mean1, cov1)
X = X1_rv.rvs(1000)
means = X.mean(axis=0)
cov = np.cov(X.T)
eigenvalues, eigenvectors = np.linalg.eig(cov)
X2_rv=multivariate_normal(means, cov)
X = X2_rv.rvs(1000)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
ax.scatter(X[:, 0], X[:, 1])
sns.kdeplot(x=X[:, 0], y=X[:, 1],color="red")

for i in range(len(eigenvectors)):
    plt.quiver(mean1[0], mean1[1], eigenvectors[:, i][0], eigenvectors[:, i][1], scale=5, color=['r', 'b'])


plt.show()