# push
def push_func(stack, item):
    stack += [item]
    return stack

# pop
def pup_fun(stack):
    if isEmpty(stack):
        return "This stack is empty"
    else:
        last_item = stack[-1]
        del stack[-1]
        return last_item


# peek
def peek_func(stack):
    if isEmpty(stack):
        return "This stack is empty"
    else:
        return stack[-1]

# check is empty
def isEmpty(stack):
    return len(stack) == 0 

stack = []

res = push_func(stack, "A")
res = push_func(stack, "B")
res = push_func(stack, "C")
res = push_func(stack, "D")
peek = peek_func(stack)
pop = pup_fun(stack)


print("stack => ", res)
print("Peek item", peek)
print("pop item", pop)


