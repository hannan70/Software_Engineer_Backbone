class MyQueue:
    def __init__(self):
        self.queue = []

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # add item inside queue
    def enqueue(self, item):
        self.queue.append(item)

    # get item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        # return the first item
        return self.queue.pop(0)

    # get the item of the queue without remove it
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        # return first item form queue
        return self.queue[0]

    # Total number of items in the queue
    def size(self):
        return len(self.queue)

    # print all items
    def print_items(self):
        for i in self.queue:
            print(i)

q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Size of queue", q.size())
print("Peek item", q.peek())

print("Remove item", q.dequeue())
print("Remove item", q.dequeue())

print("Queue is empty:", q.is_empty())
print("Remove item", q.dequeue())
print("Remove item", q.dequeue())
print("Queue is empty:", q.is_empty())

print('=========')
q.print_items()


