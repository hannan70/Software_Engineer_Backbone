
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

nums = [1, 3, 5, 6]
target = 4
print(searchInsert(nums, target))




# -- way one

# print(searchInsert(nums, target))nsert(nums, target):
#     counter = 0
#     for i in range(len(nums)):
#         if nums[i] < target:
#             counter += 1
#
#         if nums[i] == target:
#             return i
#
#     return counter
#
# nums = [1, 3, 5, 6]
# target = 4
# print(searchInsert(nums, target))