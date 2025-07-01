
def selection_sort(arr, size):

    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            (arr[i], arr[min_index]) = (arr[min_index], arr[i])


arr = [10, 5, 1, 8, 7, 2, -1, 100]
size = len(arr)
selection_sort(arr, size)
print(arr)


