




# ======== Text wrap one soluation =====

def wrap(string, max_width):

    new_string = list()
    flag = 0

    for i in list(string):
        flag += 1
        new_string.append(i)
        if flag == max_width:
            new_string.append("\n")
            flag=0

    return "".join(new_string)


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

# Text wrap solution two
import textwrap

def wrap(string, max_width):

    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.fill(text=string)

    return word_list

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

# Textwrap solution two
str = input()
w = int(input())

temp_str = str
val_list = list()
while len(temp_str) > w:
    val_str = temp_str[:w]
    temp_str = temp_str[w:]
    val_list.append(val_str)

val_list.append(temp_str)

val = '\n'.join([val for val in val_list])
print(val)


