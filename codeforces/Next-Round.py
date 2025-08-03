n, k = list(map(int, input().split()))

scores = list(map(int, input().split()))
"""
4 3
1 1 4 7 8
4 is 3rd place
"""
place = scores[k - 1]
res = 0
for i in scores:
    if i >= place and i > 0:
        res += 1

print(res)


