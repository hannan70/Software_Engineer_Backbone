
def bubble_sort(arr, size):

    for i in range(size):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])


arr = [30, 5, 10, 15, 20, -1, 100]
size = len(arr)
bubble_sort(arr, size)
print(arr)
