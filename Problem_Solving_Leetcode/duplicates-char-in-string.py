

def duplicate_char(str):
    sorted_str = ''.join(sorted(str))
    length = len(sorted_str)
    i = 0
    while i < length:
        count = 1
        while i < length - 1 and sorted_str[i] == sorted_str[i+1]:
            count += 1
            i += 1

        if count > 1:
            print(f"{sorted_str[i]} => {count}")

        i += 1


str = "geeksforgeeks"
duplicate_char(str)