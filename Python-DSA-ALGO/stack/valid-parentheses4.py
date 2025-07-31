def isValid(s: str) -> bool:
    stack = []  
    ch_map = {"(": ")", "{": "}", "[": "]"}


    for ch in s:
        if ch in "({[": 
            stack.append(ch) 
        else:
            if not stack:
                return False

            last_item = stack.pop() 
            
            # ch_map["("] = ")"
            # ")" == ")" 
            if ch_map[last_item] != ch:  #   ch_map[last_item] mane opening ta jodi ch_map[ch] closing tar sathe na mile then return false
                return False
            
             
   
    return stack == []



s = "()"
res = isValid(s)
print(res)
 