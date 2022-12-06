import numpy as np

macierz = np.random.randint(low = 0, high = 51, size = (5, 5))
print(macierz)
print("maksymalna wartosc macierzy: ", macierz.max())
print("minimalna wartosc macierzy: ", macierz.min())
print()
print("maksymalna wartossci w kazdym z wierszow: ", macierz.max(axis = 1))
print("maksymalna wartosc macierzy: ", macierz.max(axis = 0))

print("suma wirszy: ", macierz.sum(axis = 1))
