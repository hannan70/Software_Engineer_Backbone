# def containsDuplicate(nums):
#     is_duplicate = False
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[i] == nums[j]:
#                 is_duplicate = True
#                 break
    
#     if is_duplicate:
#         return True
#     else:
#         return False



# nums = [1,2,3,4]
# res = containsDuplicate(nums)
# print(res)

"""
Time Complexity: O(n log n)
Space Complexity: O(1) (if sorting in-place)
"""

# def containsDuplicate(nums):
#     nums.sort()
#     for i in range(1, len(nums)):
        
#         if nums[i] == nums[i -1]:
#             return True
        
#     # if there is not duplicate then return false
#     return False
    
# nums = [1, 1, 2, 2]
# res = containsDuplicate(nums)
# print(res)

""""
Time Complexity: O(n)
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)
    
    # if there is not duplicate then return false
    return False
         
    
nums = [1,2,3,1]
res = containsDuplicate(nums)
print(res)