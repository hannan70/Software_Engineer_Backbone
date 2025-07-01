
def isPalindrome(x):

    # Convert the number to a string
    num_str = str(x)

    # Reverse the string
    reverse_str_num = num_str[::-1]

    # Check the number palindrome or not
    if num_str == reverse_str_num:
        return True
    else:
        return False


num = -121
print(isPalindrome(num))
