# def sortArrayByParity(nums):
#     size = len(nums)

#     for i in range(0, size-1):
#         print("outer loop =====", nums[i])
#         for j in range(0, size-i-1):
#             print("inner loop", nums[j])
#             # if current is odd and next is even then swap
#             if nums[j] % 2 != 0 and nums[j+1] % 2 == 0:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
            
#     return nums


# nums = [0]
# res = sortArrayByParity(nums)
# print(res)


# way two
def sortArrayByParity(nums):
    size = len(nums) - 1
    left, right = 0, size

    while left < right:  # 1 < 2 = true

        if nums[left] % 2 == 0:
            # move left if number is even
            left += 1 
        elif nums[right] % 2 != 0:
            # move left if number is odd
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

nums = [3,1,2,4] 
# nums = [0,2,1] 


res = sortArrayByParity(nums)
print(res)




 