class Stack:
    def __init__(self):
        self.stack = []

    # push item in the stack
    def push_func(self, item):
        self.stack += [item]
        return self.stack

    # remove last item using pop function
    def pop_func(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            last_item = self.stack[-1]
            del self.stack[-1]
            return last_item

    # get last value in a stack
    def peek_func(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.stack[-1] 

    # check is empty
    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
s.push_func("A")
s.push_func("B")
s.push_func("C")
s.push_func("D")
s.push_func("E")
peek = s.peek_func()
pop = s.pop_func()

print(s.stack)
print("Peek", peek)
print("Pop", pop)