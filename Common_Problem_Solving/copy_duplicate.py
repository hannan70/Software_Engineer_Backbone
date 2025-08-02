'''
in this way:
Time Complexity: O(n²)
Space Complexity: O(1)  
'''

# def copy_duplicate(nums):
#     duplicate_list = []

#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[i] == nums[j]:
#                 duplicate_list.append(nums[i])

#     print(duplicate_list)



# nums = [10, 20, 30, 10, 30, 40, 50, 100, 50]
# copy_duplicate(nums)


'''
in this way:
Time Complexity: O(n log n)
Space Complexity: O(1) (if sorting in-place)
'''
# def copy_duplicate(nums): 
#     nums.sort()
#     duplicate_list = []
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             duplicate_list.append(nums[i])


#     print(duplicate_list)


# nums = [10, 20, 30, 10, 30, 40, 50, 100, 50]
# copy_duplicate(nums)



'''
in this way:
Time Complexity: O(n log n)
Space Complexity: O(1) (if sorting in-place)
'''
def copy_duplicate(nums): 
    seen = set()
    duplicate_list = []
    for num in nums:
        if num in seen:
            duplicate_list.append(num)

        seen.add(num)


    print(duplicate_list)

nums = [10, 20, 30, 10, 30, 40, 50, 100, 50]
copy_duplicate(nums)


