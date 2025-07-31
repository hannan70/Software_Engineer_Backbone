def isValid(s: str) -> bool:
    stack = []  
    ch_map = {")": "(", "}": "{", "]": "["}


    for ch in s:
        if ch in "({[": 
            stack.append(ch) 
        else:
            if not stack:
                return False
             
            if stack[-1] != ch_map[ch]:  # stack [ '(' != '(': 2ta same thai return false na kore true korbe ]
                return False
            
            # if match then remove item from stack
            stack.pop()
   
    return stack == []



s = "()"
res = isValid(s)
print(res)
 