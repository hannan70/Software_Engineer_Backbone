'''
Input: [1, 2, 3, 4]
Output: [1, 3, 6, 10]
'''

def cumulative_sum(nums):
    new_list = []
    total = 0  
    for num in nums:
        total += num
        new_list.append(total)

    return new_list


nums = [1,1,1,1,1]

result = cumulative_sum(nums)
print(result)