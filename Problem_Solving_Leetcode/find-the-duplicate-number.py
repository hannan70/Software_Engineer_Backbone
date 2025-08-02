def findDuplicate(nums):
    seen = set()
    duplicate = 0
    for num in nums:
        if num in seen:
            duplicate = num

        seen.add(num)

    return duplicate


nums = [3,3,3,3,3]
res = findDuplicate(nums)
print(res)