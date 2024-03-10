import numpy as np

# Generowanie losowej tablicy z wielowymiarowego rozkładu normalnego
np.random.seed(42)  # ustawienie ziarna dla powtarzalności wyników
data = np.random.multivariate_normal(mean=np.zeros(5), cov=np.eye(5), size=100)

# Normalizacja zbioru punktów
normalized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# Obliczenie średniej i macierzy kowariancji przekształconych danych
mean_normalized = np.mean(normalized_data, axis=0)
covariance_matrix = np.cov(normalized_data, rowvar=False)

print("Średnia przekształconych danych:")
print(mean_normalized)
print("\nMacierz kowariancji przekształconych danych:")
print(covariance_matrix)

# print("\n\n")
# print("Dane początkowe:")
# print(data)
# print("\nDane przekształcone:")
# print(normalized_data)
# print("\n")
