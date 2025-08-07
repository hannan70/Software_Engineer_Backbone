def intersection(nums1, nums2):
    n1 = nums1
    n2 = nums2
    new_n = set()
    for i in n2:
        if i in n1:
            new_n.add(i)

    return list(new_n)



 

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
res = intersection(nums1, nums2)
print(res)
