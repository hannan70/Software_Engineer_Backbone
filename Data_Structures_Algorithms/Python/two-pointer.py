def twoSum(nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:

            sum = nums[left_pointer] + nums[right_pointer]
            if sum == target:
                return [left_pointer+1, right_pointer+1]
            elif sum < target:
                left_pointer += 1
            else:
                right_pointer -= 1

        # it there is not solution then return empty list
        return []

nums = [2, 5, 7, 10]
target = 9
print(twoSum(nums, target))