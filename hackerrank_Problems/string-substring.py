
string = input().strip()
sub_string = input().strip()


def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)

    for i in range(0, len(string)):
        if string[i:i + sub_len] == string:
            counter += 1

    return counter

count = count_substring(string, sub_string)
print(count)
