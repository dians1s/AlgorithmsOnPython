import math

array = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9,
         6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32]

counter = 0


def quickSort(array):
    if (len(array) <= 1):
        return array
    pivotIndex = math.floor(len(array) / 2)
    pivot = array[pivotIndex]
    less = []
    greater = []
    for i in range(len(array)):
        global counter
        counter += 1
        if (i == pivotIndex):
            continue
        if (array[i] < pivot):
            less.append(array[i])
        else:
            greater.append(array[i])
    return [*quickSort(less), pivot, *quickSort(greater)]


print(quickSort(array))
print(counter)
