
def minimumOperations(nums):
    print(nums[3:])
    operations = 0
    def is_distinct(nums):
        return len(nums) == len(set(nums))

    while not is_distinct(nums):
        if len(nums) >= 3:
            nums = nums[3:]
        else:
            nums = []
        operations += 1

    return operations

nums = [4,5,6,4,4]
minimumOperations(nums)