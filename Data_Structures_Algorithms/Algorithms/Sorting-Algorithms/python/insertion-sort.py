def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        item = arr[i]  # 17
        j = i - 1  # 2-1 = 1 arr[0] = 30

        while(j >= 0 and arr[j] > item):
            arr[j+1] = arr[j]
            j = j - 1 

       
        arr[j + 1] = item
      



arr = [10, 30, 17, 1, 12, -1]  

insertion_sort(arr)

for k in arr:
    print(k, end=" ")