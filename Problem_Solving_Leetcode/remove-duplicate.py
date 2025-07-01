def remove_duplicate(numbers):
    duplicate_array = []
    i = 0
    while i < len(numbers):
        if numbers[i] in numbers[:i]:
            duplicate_array.append(numbers[i])
        i = i + 1

    print(numbers)
    print(duplicate_array)

numbers = [1, 2, 3, 4, 2, 3, 3, 5, 7]
remove_duplicate(numbers)

# def duplicate_array_make(nums):
#     seen = set()
#     duplicate_arr = set()
#     for num in nums:
#         if num in seen:
#             duplicate_arr.add(num)
#         else:
#             seen.add(num)
#
#     print(list(duplicate_arr))
#     print(list(seen))
#
#
# nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
# duplicate_array_make(nums)


# make duplicate array
# def duplicate_array_make(nums):
#     duplicate_arr = set()
#     for i in range(len(nums)):
#         if nums[i] in nums[:i]:
#             duplicate_arr.add(nums[i])
#
#     print(list(duplicate_arr))
#
#
# nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
# duplicate_array_make(nums)


# def remove_duplicate(numbers):
#     i = 0
#     while i < len(numbers):
#         if numbers[i] in numbers[:i]:
#             del numbers[i]
#         i = i + 1
#
#     print(numbers)
#
# numbers = [20, 25, 40, 20, 50, 40]
# remove_duplicate(numbers)




# def remove_duplicate(numbers):
#     unique_list = list(set(numbers))
#     print(unique_list)
# numbers = [20, 25, 40, 20, 50, 40]
# remove_duplicate(numbers)



# def remove_duplicate(numbers):
#     unique_list = []
#     for num in numbers:
#         if num not in unique_list :
#             unique_list.append(num)
#
#     print(unique_list)
#
#
#
# numbers = [20, 25, 40, 20, 50, 40]
# remove_duplicate(numbers)