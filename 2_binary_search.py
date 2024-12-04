import math

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

counter = 0
counterRecursive = 0


def binarySearch(array, item):
    start = 0
    end = len(array)
    found = False
    position = -1
    if (not item in array):
        return 'Not in array'
    while (found == False and start <= end):
        global counter
        counter += 1
        middle = math.floor((start + end) / 2)
        if (array[middle] == item):
            found = True
            position = middle
            return position
        if item < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return position


def recursiveBinarySearch(array, item, start, end):
    global counterRecursive
    if (not item in array):
        return 'Not in array'
    middle = math.floor((start + end) / 2)
    counterRecursive += 1
    if (item == array[middle]):
        return middle
    if (item < array[middle]):
        return recursiveBinarySearch(array, item, 0, middle - 1)
    else:
        return recursiveBinarySearch(array, item, middle + 1, end)


print(binarySearch(array, 14))
print(counter)

print(recursiveBinarySearch(array, 14, 0, len(array)))
print(counterRecursive)
