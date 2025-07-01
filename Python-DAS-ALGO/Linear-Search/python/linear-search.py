
def linear_search(arr, item):
    for i in range(len(arr)):
         if arr[i] == item:
             return i

    return -1


arr = [30, 10, 33, 24, 20]
item = 24
index = linear_search(arr, item)

if index == -1:
    print("Item not found")
else:
    print("Item found at index ", index)
