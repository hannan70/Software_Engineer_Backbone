def swap_case(s):
    res = []
    for str in string:
        if str.isupper():
            res.append(str.lower())
        else:
            res.append(str.upper())

    return ''.join(res)


string = input()
print(swap_case(string))

