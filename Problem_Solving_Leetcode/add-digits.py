def addDigits(num):
    total = 0
    while num > 0:
        reminder = num % 10
        total += reminder
        num //= 10

    if len(str(total)) == 1:
        return total
    else:
        return addDigits(total)


num = 38
print(addDigits(num))