arr = [99, 23, 11, 45]

length = len(arr)


def bubblesort(array):
    for j in range(0,length-1):
        for i in range(0,length-1-j):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    return array


hello = bubblesort(arr)
print(hello)