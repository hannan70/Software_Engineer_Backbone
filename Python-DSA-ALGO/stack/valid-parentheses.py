def isValid(s: str) -> bool:
    stack = []  
    for ch in s:
        if ch in "({[": 
            stack.append(ch) 
        else: 
            if len(stack) == 0:
                return False
            
            last_item = stack.pop() # ( 

            if ch == ")":
                if last_item != "(": # ( != )
                    return False
            elif ch == "}":
                if last_item != "{":
                    return False
            elif ch == "]":
                if last_item != "[":
                    return False
               
   
    return stack == []



s = "())"
res = isValid(s)
print(res)
 