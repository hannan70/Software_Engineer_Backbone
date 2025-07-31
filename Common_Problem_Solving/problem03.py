nums = list(map(int, input().split()))
 
def get_number_status(nums):
     
    for num in nums:
        if num == 0:
            print("null")
        if num % 2 == 0 and num > 0:
            print("Even Positive")
        elif num % 2 == 0 and num < 0 :
            print("Even Negative")
        elif num % 2 != 0 and num > 0:
            print("Odd Positive")
        elif num % 2 != 0 and num < 0:
            print("Odd Negative")

get_number_status(nums)
 