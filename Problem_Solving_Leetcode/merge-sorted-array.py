def merge(nums1, m, nums2, n):

    # last index
    last_index = m + n - 1
    a = m - 1
    b = n - 1
    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[last_index] = nums1[a]
            a -= 1
        else:
            nums1[last_index] = nums2[b]
            b -= 1

        last_index -= 1


     # for i, j in enumerate(range(m, m+n)):
     #     nums1[j] = nums2[i]
     #
     # nums1.sort()
     # return nums1




# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
res = merge(nums1, m, nums2, n)
print(res)