import itertools
import sys

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

def generateIndexes(list: tablica):
    """
    Generates possible indexes based on every single starting point and added diagonals
    in: 2d array of numbers
    out: array of arrays - every element of this array represents possible indexes to walk through from given starting point.
    """
    indexes_array = []
    for startingpoint in range(len(tablica)):
        diagonals = [startingpoint]
        indexes_array.append([[startingpoint]])
        for column in range(len(tablica[0])-1):
            getdiagonals(diagonals)
            indexes_array[-1].append(diagonals[::])
    return indexes_array

def getPaths(array):
    paths = [list(i) for j in range(len(array)) for i in itertools.product(*array[j])]
    return paths
    
def isValid(path):
    for i in range(len(path)-1):
        if abs(path[i] - path[i+1]) > 1:
            return False
    return True
    
def removeIllegalPaths(array):
    temp_array = []
    for way in array:
        if isValid(way):
            temp_array.append(way)
    return temp_array    
    
def calculatePoints(path, array):
    """
    in: path - the 1d array of indexes
        array - 2d array filled with numbers
    out: sum of the certain indexes values in 2d array
    """
    my_sum = 0
    for column in range(len(path)):
        my_sum += array[path[column]][column]
    return my_sum
    
min_sum = sys.maxsize
min_path = []
my_arr = generateIndexes(tablica)
my_ways = getPaths(my_arr)
my_ways = removeIllegalPaths(my_ways)


for way in my_ways:
    path_sum = calculatePoints(way, tablica)
    if path_sum < min_sum:
        min_sum = path_sum
        min_path = way

print(min_path, min_sum)