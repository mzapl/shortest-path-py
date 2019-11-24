tablica = [
    [6, 2, 6, 1, 7],
    [4, 9, 5, 5, 8],
    [3, 1, 4, 5, 6]
]

def getdiagonals(diagonals, height = len(tablica)):
    mymin, mymax = min(diagonals), max(diagonals)
    if mymin > 0:
        diagonals.append(mymin - 1)
    if mymax + 1< height:
        diagonals.append(mymax + 1)

my_arr = []
for startingpoint in range(len(tablica)):
    diagonals = [startingpoint]
    my_arr.append([[startingpoint]])
    for column in range(len(tablica[0])-1):
        getdiagonals(diagonals)
        my_arr[-1].append(diagonals[::])

for x in my_arr:
    print(x)

import itertools
z = [i for j in range(len(my_arr)) for i in itertools.product(*my_arr[j])]
print(z[0])
print([tablica])