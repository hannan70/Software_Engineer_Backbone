# problem
# def countWays(nums):
#     count = 0
#     sorted_nums = sorted(nums)
#     n = len(sorted_nums)
#
#     for k in range(n + 1):  # k = 0 থেকে n পর্যন্ত চেক
#         if (k == 0 or sorted_nums[k - 1] < k) and (k == n or k <= sorted_nums[k]):
#             count += 1
#
#     return count
#
#
# # nums = [1, 1]
# # nums = [1,1,0,1]
# nums = [6, 0, 3, 3, 6, 7, 2, 7]
# print(countWays(nums))