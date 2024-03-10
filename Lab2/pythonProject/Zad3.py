import numpy as np

# Wypełni 100-elementową tablicę liczbami losowymi naturalnymi z zakresu  $[5,15]$  i policz liczbę wystąpień tych liczb. Która z tych liczb najczęściej występuje w tak wygenerowanej tablicy?
# Wskazówka: zobacz funkcje: bincount, argmax.

data = np.random.randint(5, 16, 100)
print(data)

print(np.bincount(data))
print(np.argmax(np.bincount(data)))
print(np.bincount(data).argmax())
