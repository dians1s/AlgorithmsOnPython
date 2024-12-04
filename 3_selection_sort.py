array = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9,
         6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32]

counter = 0


def selectionSort(array):
    for i in range(len(array)):
        indexMin = i
        for j in range(i + 1, len(array)):
            global counter
            if (array[j] < array[indexMin]):
                indexMin = j
            counter += 1
        array[i], array[indexMin] = array[indexMin], array[i]
    return array


print(selectionSort(array))
print(counter)
