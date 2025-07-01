
def isValid(s):
    stack = []
    dict = { ")":"(", "}": "{", "]": "[" }

    for i in s:
        print(i)
        # if (i) is an opening bracket
        if i in dict.values():
            stack.append(i)
        else:
            # If (i) is a closing bracket
            if stack and stack[-1] == dict[i]:
                stack.pop()
            else:
                return False

    return True if not stack else False



s = "(())"
print(isValid(s))

'''
In Python, the "top item" of a list depends on the context:
If you consider the first item as "top" (like a queue):
The first item in the list is 'a1'.
    list = ['a1', 'b1', 'c1', 'd1']
    top_item = list[0]  # 'a1'
    
If you consider the last item as "top" (like a stack):
The last item in the list is 'd1'.
list = ['a1', 'b1', 'c1', 'd1']
top_item = list[-1]  # 'd1'

'''