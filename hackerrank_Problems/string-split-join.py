
line = input()

def split_and_join(line):
    split_str = line.split(" ")
    join_str = '-'.join(split_str)
    return join_str

result = split_and_join(line)
print(result)
