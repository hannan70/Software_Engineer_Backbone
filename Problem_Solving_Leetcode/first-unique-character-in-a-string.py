import collections

def firstUniqChar(s):
    count = collections.Counter(s)
    for index, char in enumerate(s):
        if count[char] == 1:
            return index
    return -1

s = "loveleetcode"
print(firstUniqChar(s))



# def firstUniqChar(s):
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char, 0) + 1
#
#
#     for index, char in enumerate(s):
#         if counts[char] == 1:
#             return index
#
#
#     return -1
#
#
# s = "bd"
# print(firstUniqChar(s))













#
# class MyQueue:
#     def __init__(self):
#         self.queue = []
#
#     # add item inside queue
#     def enqueue(self, item):
#         for i in item:
#             self.queue.append(i)
#
#     # remove item from queue
#     def dequeue(self):
#         for i in range(0, len(self.queue)):
#             if self.queue[i] in self.queue[:i]:
#                 print(self.queue[0])
#
#
#
# q = MyQueue()
#
# q.enqueue("loveleetcode")
#
#
# q.dequeue() # 10
#
#
#
#
#
#
