## Reguła Trzech Sigm
# Reguła Trzech Sigm dla danego rozkładu normalnego $N(mean,\sigma)$ oznacza, że w przedziale $[mean-3\sigma,mean+3\sigma]$ znajduje się 99.7\% wszystkich obserwacji.
#
# Napisz program, który:
#
#   * rysuje gęstość rozkładu normalnego o zadanych parametrach $mean$ i $\sigma$,
#   * wylicza pole pod krzywą
#   * zaznacza obszar po krzywą
#
# Policz prawdopodobieństwa:
#
#   * $P(X \in [mean-\sigma,mean+\sigma])$
#   * $P(X \in [mean-2\sigma,mean+2\sigma])$
#   * $P(X \in [mean-3\sigma,mean+3\sigma])$

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametry rozkładu normalnego
mean = 0
sigma = 1

# Tworzenie danych do rysowania gęstości rozkładu normalnego
x = np.linspace(mean - 4 * sigma, mean + 4 * sigma, 1000)
y = norm.pdf(x, mean, sigma)

# Rysowanie gęstości rozkładu normalnego
plt.plot(x, y, 'b-', label='N(mean, sigma)')

# Obliczanie pola pod krzywą
area = norm.cdf(mean + 3 * sigma, mean, sigma) - norm.cdf(mean - 3 * sigma, mean, sigma)
print("Pole pod krzywą: {:.4f}".format(area))

# Zaznaczanie obszaru pod krzywą
plt.fill_between(x, 0, y, where=(x >= mean - 3 * sigma) & (x <= mean + 3 * sigma), color='gray', alpha=0.5)

# Zaznaczenie obszarów prawdopodobieństw
prob_1sigma = norm.cdf(mean + sigma, mean, sigma) - norm.cdf(mean - sigma, mean, sigma)
prob_2sigma = norm.cdf(mean + 2 * sigma, mean, sigma) - norm.cdf(mean - 2 * sigma, mean, sigma)
prob_3sigma = area

print("P(X in [mean-sigma, mean+sigma]): {:.4f}".format(prob_1sigma))
print("P(X in [mean-2*sigma, mean+2*sigma]): {:.4f}".format(prob_2sigma))
print("P(X in [mean-3*sigma, mean+3*sigma]): {:.4f}".format(prob_3sigma))

plt.show()
