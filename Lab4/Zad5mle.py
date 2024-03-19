import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy import optimize

# Zadanie 5
# Policz MLE dla danych z rozkładu jednostajnego i parametrów:
# <ul>
# <li>$\mu=0$, $\sigma=1$</li>
# <li>$\mu=0$, $\sigma=2$</li>
# <li>$\mu=1$, $\sigma=1$</li>
# <li>$\mu=0.5$, $\sigma=0.2$</li>
# </ul>
# Dla których wartości wychodzi wynik największy i dlaczego?

n = 10000

# Losowanie próbki z rozkładu jednostajnego

data = np.random.uniform(-1,1,n)

# Obliczenie parametrów rozkładu normalnego
mu = np.mean(data)
sigma = np.std(data)

# Rysowanie histogramu próbki
sns.histplot(data, kde=False, stat='density')

# Obliczenie MLE dla danych z rozkładu jednostajnego i parametrów:

# $\mu=0$, $\sigma=1$
mu1 = 0
sigma1 = 1
mu1_mle = np.mean(data)
sigma1_mle = np.std(data)

# $\mu=0$, $\sigma=2$
mu2 = 0
sigma2 = 2
mu2_mle = np.mean(data)
sigma2_mle = np.std(data)

# $\mu=1$, $\sigma=1$
mu3 = 1
sigma3 = 1
mu3_mle = np.mean(data)
sigma3_mle = np.std(data)

# $\mu=0.5$, $\sigma=0.2$
mu4 = 0.5
sigma4 = 0.2
mu4_mle = np.mean(data)
sigma4_mle = np.std(data)

# Rysowanie funkcji gęstości rozkładu normalnego
t = np.linspace(-2,2,1000)

plt.plot(t, stats.norm.pdf(t, mu1, sigma1), 'k-', lw=2, label='Rozkład normalny ($\mu=0$, $\sigma=1$)')
plt.plot(t, stats.norm.pdf(t, mu2, sigma2), 'r-', lw=2, label='Rozkład normalny ($\mu=0$, $\sigma=2$)')
plt.plot(t, stats.norm.pdf(t, mu3, sigma3), 'g-', lw=2, label='Rozkład normalny ($\mu=1$, $\sigma=1$)')
plt.plot(t, stats.norm.pdf(t, mu4, sigma4), 'b-', lw=2, label='Rozkład normalny ($\mu=0.5$, $\sigma=0.2)')
plt.legend()

# Dodanie legendy i tytułu
plt.legend()
plt.title('Porównanie próbki jednostajnej i rozkładu normalnego')
plt.show()
