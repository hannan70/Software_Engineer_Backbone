def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort() 
    res = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums1[j]:
            i += 1
        else:
            j += 1

    return res

nums1 = [1,2,2,1]
nums2 = [2,2] 
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

res = intersection(nums1, nums2)
print(res)



# def intersection(nums1, nums2):
#     from collections import Counter
#     count1 = Counter(nums1)
#     res = []

#     for num in nums2:  
#         if count1[num] > 0:
#             res.append(num)
#             count1[num] -= 1
#     return res


# # nums1 = [1,2,2,1]
# # nums2 = [2,2,2] 
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# res = intersection(nums1, nums2)
# print(res)
