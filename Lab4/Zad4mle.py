import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy import optimize

# Zadanie 4

# Wiemy, że funkcja wiarygodnosci ma postać:
#
# $$
# L(X,m,\sigma)=\prod_{i=1}^n f_{m,\sigma} (x_i).
# $$
#
#
# Zaimplementuj logarytmiczną funkcję wiarygodności  dla rodziny rozkładów normalnych:
#
# $$
# l(X,m,\sigma)=\ln\left( L(X,m,\sigma) \right)=\ln\left(\prod_{i=1}^n f_{m,\sigma} (x_i) \right)=\sum_{i=1}^n \ln(f_{m,\sigma} (x_i))
# $$

# split normal distribution pdf
def Gpdf(x, mu, sigma):
    return 1/(sigma * (2*np.pi)**.5) *np.e ** (-(x-mu)**2/(2 * sigma**2))

# log likelihood function
def log_likelihood(params, x):
    mu, sigma = params
    return -np.sum(np.log(Gpdf(x, mu, sigma)))

# generate data
n = 1000
data = np.random.normal(0,1,n)

# fit data to normal distribution
mu, sigma = stats.norm.fit(data)

# fit data to normal distribution using log likelihood function
params0 = [mu, sigma]
result = optimize.minimize(log_likelihood, params0, args=(data))
mu_ml, sigma_ml = result.x

# plot data
t = np.linspace(-3,3,1000)
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram próbki normalnej')
# plt.plot(t, stats.norm.pdf(t, mu, sigma), 'k-', lw=2, label='Rozkład normalny ($\mu=1$, $\sigma=1$)')
plt.plot(t, stats.norm.pdf(t, mu_ml, sigma_ml), 'r-', lw=2, label='Rozkład normalny ($\mu_{ml}$, $\sigma_{ml}$)')
plt.legend()
plt.title('Porównanie próbki normalnej i rozkładu normalnego')
plt.show()