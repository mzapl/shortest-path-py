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

for startingpoint in range(len(tablica)):
    diagonals = [startingpoint]
    for column in range(len(tablica[0])):
        print(diagonals)
        getdiagonals(diagonals)
