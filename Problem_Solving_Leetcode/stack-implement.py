CAPACITY = 4
stack = []
top = -1

# add items
def my_push(x):
    global top
    if top < CAPACITY - 1:
        top += 1
        stack.append(x)
        print(f"Item added {x}")
    else:
        print("Not Spaces")


def my_pop():
    global top
    if top >= 0:
        val = stack.pop()
        top -= 1
        print(f"Pop items {val}")
    else:
        print("Empty Stack")

# peek items
def peek():
    if top >= 0:
        return stack[top]
    else:
        print("Empty Stack")

my_push(10)
my_push(20)
my_push(30)
my_push(40)
my_pop()
my_push(50)
print(f"Peek items: {peek()}")
