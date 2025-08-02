def count_single(nums):
    dist = {}
    for i in nums: 
        if i in dist:
            dist[i] += 1
        else:
            dist[i] = 1 
    
    for key, val in dist.items():
        if val == 1:
            print(key)
             

nums = [1, 2, 2]  # ANS: 1
count_single(nums)

# way two (using XOR)
def find_single(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


nums = [2,2,3]
result = find_single(nums)
print(result) # 3