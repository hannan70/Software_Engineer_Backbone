def miniMaxSum(arr):
    arr.sort()
    arr_min = 0
    arr_max = 0
    for i in range(4):
        arr_min += arr[i]
        arr_max += arr[4-i]
    print(f"{arr_min} {arr_max}")

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
