def climbStairs(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n+1):
        current = first + second
        first = second
        second = current

    return second

n = 4
print(climbStairs(n))
