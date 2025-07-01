def validPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            str1 = s[:l]+s[l+1:]
            str2 = s[:r]+s[r+1:]
            return str1==str1[::-1] or str2==str2[::-1]
        l += 1
        r -= 1
    return True

s = "abca"
print(validPalindrome(s))