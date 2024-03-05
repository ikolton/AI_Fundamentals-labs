import numpy as np
import random

def dist(x):
    return np.sqrt(np.sum(x**2, axis=1))

#wygeneruj losową tablicę 100x10 która będzie reprezentować 100 punktów w 10 wymiarowej przestrzenii

#random array
x = np.random.rand(100,10)



#print(x)

#napisz funkcję która policzy odległość euklidesową pomiędzy każdą parą punktów bez użycia pętli



print(dist(x))

