def repeatedCharacter(s):
    char_dict = {}
    for char in s:
        if char_dict.get(char):
            return char
        else:
            char_dict[char] = 1


s = "abccbaacz"
# s="nwcn" # output n
print(repeatedCharacter(s))