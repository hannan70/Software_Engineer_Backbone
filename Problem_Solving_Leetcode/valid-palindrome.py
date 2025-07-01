def isPalindrome(s):
    cleaned_text = ''.join(char for char in s if char.isalnum()).lower()
    return cleaned_text[::-1] == cleaned_text



s = "race a car"
print(isPalindrome(s))