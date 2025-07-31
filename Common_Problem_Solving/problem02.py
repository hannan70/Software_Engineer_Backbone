n = int(input())

new_list = []
for num in range(1, 41):
    if num % n == 2:
        new_list.append(num)


print(new_list)