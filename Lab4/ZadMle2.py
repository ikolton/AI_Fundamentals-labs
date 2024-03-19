# Zadanie 2
# Napisz program, który losuje próbkę z rozkładu jednostajnego i rysuje funkcję gęstości rozkładu normalnego z parametrami
#
# <ul>
# <li>$\mu=\frac{1}{n}\sum_{i=1}^n x_i$</li>
# <li>$\sigma^2=\frac{1}{n} \sum_{i=1}^n(x_i - \mu)^2$</li>
# </ul>

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy import optimize

n = 10000

# Losowanie próbki z rozkładu jednostajnego
data = np.random.uniform(-1,1,n)

# Obliczenie parametrów rozkładu normalnego
mu = np.mean(data)
sigma = np.std(data)

# Rysowanie histogramu próbki
sns.histplot(data, kde=False, stat='density')
