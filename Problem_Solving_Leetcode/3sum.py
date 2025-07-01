from types import new_class


def threeSum(nums):
    nums.sort()
    new_list = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = [nums[i], nums[j], nums[k]]
                    if trip not in new_list:
                        new_list.append(trip)

    return new_list

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

# [[-1,-1,2],[-1,0,1]]