array = [1, 4, 5, 8, 5, 1, 2, 7, 5, 2, 11]

counter = 0


def linearSearch(array, item):
    for i in range(len(array)):
        global counter
        counter += 1
        if (array[i] == item):
            return i
    return None


print(linearSearch(array, 5))
print(counter)
