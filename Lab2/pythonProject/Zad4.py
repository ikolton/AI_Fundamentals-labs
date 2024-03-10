import numpy as np

# Korzystając z poniższego kodu zaimportuj dane **breast cancer**, który składa się z 2 elementów: macierzy  $X$  o wymiarach 569 x 30 oraz wektora  $y$ o długości 569. Macierz  $X$  opisuje badania 683 pacjentów, a wektor  $y$  ich diagnozy.

from sklearn.datasets import load_breast_cancer
X, y  = load_breast_cancer(return_X_y=True)
# print(X.shape)
# print(y.shape)

# Za pomocą biblioteki **numpy** przenumeruj wektor  $y$ , tzn zamień wartości $0$ i $1$ na $-1$ i $+1$. Przeskaluj macierz  $X$ , tak żeby wartości w każdej kolumnie mieściły się w zakresie  $[0,1]$ , innymi słowy przeskaluj niezależnie każdą kolumnę  $X_i$  według poniższej procedury:
#
# $$
# X_i=\frac{X_i-min(X_i)}{max(X_i)-min(X_i)}.
# $$

y = np.where(y == 0, -1, 1)
X = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))
print(X)
print(y)