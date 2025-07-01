

def plusOne(digits):
    # reversed order

    for i in range(len(digits) - 1, -1, -1):
        # if there is no carry
        if digits[i] + 1 < 10:
            digits[i] += 1
            return digits

        digits[i] = 0

        if i == 0:
            return [1] + digits


digits = [1,2,3]
print(plusOne(digits))




# def plusOne(digits):
#     str_list = ""
#     for i in digits:
#         str_list += str(i)
#     numbers = int(str_list) + 1
#     return [int(num) for num in str(numbers)]
#
# digits = [9, 9]
# print(plusOne(digits))