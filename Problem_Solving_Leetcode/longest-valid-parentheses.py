

def longestValidParentheses(s):
    left = right = max_length = 0
    # Left-to-right traversal
    for ch in s:
        if ch == "(":
            left += 1
        else:
            right += 1
        if left == right:
            max_length = max(max_length, 2 * right)
        elif right > left:
            left = right = 0

    return max_length

# s = ")()())" # 4
s = "()(()" # 2
result = longestValidParentheses(s)
print(result)

# def longestValidParentheses(s):
#     stack = [-1]
#     max_length = 0
#     for i, ch in enumerate(s):
#         if ch == "(":
#             stack.append(i)
#         else:
#             stack.pop()
#             if not stack:
#                 stack.append(i)
#             else:
#                 max_length = max(max_length, i - stack[-1])
#
#     return max_length
#
# s = ")()())" # 4
# # s = "()(()" # 2
# result = longestValidParentheses(s)
# print(result)