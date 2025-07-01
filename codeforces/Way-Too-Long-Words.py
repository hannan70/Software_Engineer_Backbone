n = int(input())

for i in range(n):
    s = input()
    if len(s) > 10:
        fl = s[0]
        ll = s[-1]
        str_len = len(s) - 2
        print(f"{fl}{str_len}{ll}")
    else:
        print(s)