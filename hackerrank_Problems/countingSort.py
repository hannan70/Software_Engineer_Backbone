def countingSort(arr):
    frequency = [0] * 100

    for num in arr:
        frequency[num] += 1

    return frequency


arr = list(map(int, input().rstrip().split()))

res = countingSort(arr)
print(res)
