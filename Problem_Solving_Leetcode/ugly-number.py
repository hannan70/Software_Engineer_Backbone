def isUgly(n):
    # if n <= 0:
    #     return False
    # for prime in [2, 3, 5]:
    #     while n % prime == 0:
    #         n //= prime
    # return n == 1

    if n == 0:
        return False
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5

    return list


n = 10 # false
# n = 8 # true
print(isUgly(n))