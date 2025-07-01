# def canBeEqual(target, arr):
#     return sorted(target) == sorted(arr)
#
# target = [3,7,9]
# arr = [3,7,11]
# print(canBeEqual(target, arr))
from collections import Counter


# def canBeEqual(target, arr):
#     m, n = len(target), len(arr)
#
#     if m != n:
#         return False
#     t = Counter(target)
#     a = Counter(arr)
#
#     for k, v in a.items():
#         if k in t and v == t[k]:
#             continue
#         else:
#             return False
#
#     return True
#
#
# target = [3,11, 7]
# arr = [3,7,11]
# print(canBeEqual(target, arr))

