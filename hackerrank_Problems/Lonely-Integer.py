def lonelyinteger(arr):

    for i in arr:
        count = arr.count(i)
        if count == 1:
            result = i
        else:
            pass
    return result


arr = [1, 2 ,3, 4, 1, 2, 3, 5]
res = lonelyinteger(arr)
print(res)
