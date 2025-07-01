
n, m = map(int, input().split())
text = "WELCOME"
a = ".|."

for i in range(n//2):
    print((a*i).rjust((m - 3) // 2, "-") + a + (a*i).ljust((m - 3) // 2, "-"))

print(text.center(m, "-"))
for i in range(n//2):
    j = n // 2 - 1 - i
    print((a*j).rjust((m - 3) // 2, "-") + a + (a*j).ljust((m - 3) // 2, "-"))
