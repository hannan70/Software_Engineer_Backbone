def LongestValidParentheses(s: str):
    stack = [3, 4]
    max_len = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()  
            if not stack:
                stack.append(i)
            else:
                valid_len = i - stack[-1] # [ 5 - 3 ]
                max_len = max(max_len, valid_len)  # 2
   
    print(stack)
    return max_len




s = ")())()()())"


print(LongestValidParentheses(s))