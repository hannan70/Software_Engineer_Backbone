def singleNumber(nums):
    new_number = 0
    for i in nums:
        new_number ^= i

    return new_number


nums = [4,1,2,1,2]
res = singleNumber(nums)
