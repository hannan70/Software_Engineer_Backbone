def findSum(numbers, queries):
    a = [0]
    b = [0]
    for x in numbers:
        a.append(a[-1] + x)
        b.append(b[-1] + (x == 0))

    # return [a[r] - a[l - 1] + x * (b[r] - b[l - 1]) for l, r, x in queries]




numbers = [20, 30, 0, 10]
queries = [[2, 2, 20]]
findSum(numbers, queries)