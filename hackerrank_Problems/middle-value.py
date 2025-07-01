

def find_middle(lst):
    lst.sort()
    length = len(lst)

    if length % 2 != 0:
        middle_index = length // 2
        return lst[middle_index]

    else:
        first_middle_index = length // 2 - 1
        second_middle_index = length // 2
        return(lst[first_middle_index], lst[second_middle_index])


lst = [1, 2, 3, 4, 5, 6]
print(find_middle(lst))
