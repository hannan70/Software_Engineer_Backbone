def subarraySum(nums):
    n = len(nums)
    total = 0
    for i in range(n):
        start = max(0, i - nums[i])
        subarray = sum(nums[start: i + 1])
        total += subarray
    return total

nums = [2,3,1]
print(subarraySum(nums))