import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Definicja parametrów
m = np.array([0, 0])
Sigma = np.array([[4.40, -2.75], [-2.75, 5.50]])

# Obliczenie wartości własnych i wektorów własnych macierzy kowariancji
eigenvalues, eigenvectors = np.linalg.eig(Sigma)

# Generowanie próbki z rozkładu normalnego
np.random.seed(0)
sample = np.random.multivariate_normal(m, Sigma, size=1000)

# Narysowanie próbki i poziomic rozkładu normalnego
plt.figure(figsize=(8, 8))
plt.scatter(sample[:, 0], sample[:, 1], alpha=0.5, label='Próbka')

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))
rv = stats.multivariate_normal(mean=m, cov=Sigma)
plt.contour(X, Y, rv.pdf(pos), cmap='viridis', levels=5)

# Narysowanie wektorów własnych
for i in range(len(eigenvectors)):
    plt.quiver(m[0], m[1], eigenvectors[:, i][0], eigenvectors[:, i][1], scale=5, color=['r', 'b'])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Próbka, poziomice i wektory własne macierzy kowariancji')
plt.grid(True)
plt.axis('equal')
plt.show()
