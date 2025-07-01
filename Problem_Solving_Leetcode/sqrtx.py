def mySqrt(num):

    if num <= 1:
        return num

    low = 1
    high = num

    while low <= high:
        mid = (low+high) // 2 # calculate mid
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            low = mid + 1
        else:
            high = mid - 1

    return high


num = 8
print(mySqrt(num))