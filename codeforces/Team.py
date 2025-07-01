from os.path import curdir

n = int(input())
count = []
for i in range(n):
    k = input().split()
    if k.count('1') >= 2:
        count.append(1)

print(len(count))

# way two
# for i in range(n):
#     nn = input().split()
#     sum = 0
#     for k in nn:
#         sum += int(k)
#     if sum >= 2:
#         count.append(sum)
#
# print(len(count))


