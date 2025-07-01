
# -- brute force
def strStr(haystack, needle):
    haystack_length = len(haystack)
    needle_length = len(needle)

    for i in range(haystack_length):

        if haystack[i: i+needle_length] == needle:
            return i

    return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))

# -- way two

# def strStr(haystack, needle):
#     if needle in haystack:
#         return haystack.index(needle)
#     else:
#         return -1
#
#
# haystack = "butsad"
# needle = "sad"
# print(strStr(haystack, needle))