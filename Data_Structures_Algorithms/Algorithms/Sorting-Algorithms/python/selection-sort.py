# the code is work but not optimal
# def selection_sort(arr):
#     size = len(arr)
#     for i in range(size):
#         print("outer loop -----------> ", arr[i])
#         for  j in range(i+1, size):
#             print("inner loop --> ", arr[j])
#             if arr[i] > arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp

#     return arr

# arr = [10, 2, 17, 1, 12, -1]  
# res = selection_sort(arr)
# print(res)


# this is optimal code
def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i #  
        for  j in range(i+1, size): 
            if arr[min_index] > arr[j]:
                min_index = j

        # Only one swap per outer loop
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [10, 2, 17, 1, 12, -1]  
res = selection_sort(arr)
print(res)