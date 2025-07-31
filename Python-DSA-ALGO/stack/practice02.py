size = 5
stack = [None] * size
top = -1

def push_item(stack, size, top, item):
    if top > size:
        print("stack overflow")
        return top

    top += 1
    stack[top] = item

    return top


def pop_item(stack, top):
    if isempty(top):
        print("The stack is empty")
    last_item = top
    top -= 1
    return last_item, top



def peek_item(stack, top):
    if isempty(top):
        print("The stack is empty")
    else:
        return stack[top]


def isempty(top):
    return top == -1


top = push_item(stack, size, top, "A")
top = push_item(stack, size, top, "B")
top = push_item(stack, size, top, "C")
top = push_item(stack, size, top, "D")
top = push_item(stack, size, top, "E") 
print("Stack after push", stack[:top+1])

print("Peek Item", peek_item(stack, top))

last_item, top = pop_item(stack, top) 
print("Pop item", stack[last_item])
print("Stack item after pop", stack[:top+1])