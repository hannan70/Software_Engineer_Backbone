
def bubble_sort(arr, size):
    for i in range(size):
        swap = 0
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                swap = 1

        if swap == 0:
            break


arr = [200, 1, 30, 15, 40, 12, -1, 300]
size = len(arr)
bubble_sort(arr, size)
print(arr)
