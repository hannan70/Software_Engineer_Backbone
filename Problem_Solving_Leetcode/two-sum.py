
def twoSum(nums, target):

    for i in range(len(nums)):
        first_number = nums[i]
        for j in range(i+1, len(nums)):
            second_number = nums[j]
            if first_number + second_number == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
