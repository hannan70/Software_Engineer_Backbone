
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if self.minStack:
            item = min(val, self.minStack[-1])
        else:
            item = min(val, val)
        self.minStack.append(item)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

    def printall(self):
        for i in self.minStack:
            print(i)


s = MinStack()

s.push(-2)
s.push(0)
s.push(-3)
s.push(-10)
s.push(0)
s.push(-20)
s.printall()


