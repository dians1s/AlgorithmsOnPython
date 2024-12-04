array = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9,
         6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32]

counter = 0


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            global counter
            if (array[j + 1] < array[j]):
                array[j], array[j + 1] = array[j + 1], array[j]
            counter += 1
    return array


print(bubbleSort(array))
print(counter)
