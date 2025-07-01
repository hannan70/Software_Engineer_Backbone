
def add_two_numbers(l1, l2):
    l1_str = ""
    l2_str = ""

    for i in reversed(l1):
        l1_str += str(i)

    for j in reversed(l2):
        l2_str += str(j)


    total = int(l1_str) + int(l2_str)

    new_list = list(map(int, str(total)))
    new_list.reverse()
    return new_list


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(add_two_numbers(l1, l2))