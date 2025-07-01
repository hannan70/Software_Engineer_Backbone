def nthUglyNumber(n):

    ugly_number = [0] * n
    ugly_number[0] = 1
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5

    for i in range(1, n):
        ugly_number[i] = min(next2, next3, next5)

        if ugly_number[i] == next2:
            i2 += 1
            next2 = ugly_number[i2]*2
        if ugly_number[i] == next3:
            i3 += 1
            next3 = ugly_number[i3]*3
        if ugly_number[i] == next5:
            i5 += 1
            next5 = ugly_number[i5]*5



n = 12
print(nthUglyNumber(n))