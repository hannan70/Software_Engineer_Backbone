def longestValidParentheses(s: str) -> int:
    stack = [-1] 
    max_len = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)

        else:
            stack.pop()  
            if not stack:
                stack.append(i)

            else:
                valid_len = i - stack[-1]  
                max_len = max(max_len, valid_len)  


    return max_len

      

s = "(()" # 2
# s = ")()())" # 4
# s = "" # 0

# s = "()(())"
# s = ")(" # 0

print(longestValidParentheses(s))