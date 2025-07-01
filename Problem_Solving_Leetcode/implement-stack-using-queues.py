
class MyStack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        if item:
            self.stack.append(item)

    def pop(self):
        if self.stack != 0:
            return self.stack.pop()

    def top(self):
        if self.stack != 0:
            return self.stack[-1]

    def empty(self):
        if self.stack == 0:
            return True
        else:
            return False


stack = MyStack()
stack.push(1)
stack.push(2)

print(stack.top())
print(stack.pop())
stack.pop()
print(stack.empty())

