n = int(input())

x = 0

for i in range(0, n):
    char = input()
    if char == "++X" or char == "X++":
        x += 1
    elif char == "X--" or char == "--X":
        x -= 1
    else:
        x = 0

print(x)

 