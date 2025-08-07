def sortColors(nums):
    size = len(nums)

    for i in range(0, size-1):
        swap = 0
        for j in range(0, size-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = 1

        if swap == 0:
            break

    return nums



nums = [2,0,1]
sortColors(nums)
for k in nums:
    print(k, end=" ")