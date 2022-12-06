import numpy as np

tab = [2**i for i in range (7, -1, -1)]
print(tab)

wagi = np.array(tab)
print(wagi)

liczba_bin = np.random.randint(low = 0, high = 2, size = (8))
print(liczba_bin)

a = (wagi * liczba_bin)
print(a)

print("suma liczby binarnej w forjme decymalnej: ", a.sum())

