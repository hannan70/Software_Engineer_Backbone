

def lengthOfLastWord(s):
    split_str = s.strip().split(" ")
    print(len(split_str[-1]))


s = "luffy joyboy is still"
lengthOfLastWord(s)
# def lengthOfLastWord(s):
#     split_str = s.strip().split(" ")
#     max = -1
#     for i in split_str:
#         max = len(i)
#         if max > len(i):
#             max = i
#
#     return max
#
#
# s = "luffy is still joyboy"
# lengthOfLastWord(s)