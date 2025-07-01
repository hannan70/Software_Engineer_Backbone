def timeConversion(s):
    period = s[-2:]
    hour = s[:2]
    if (period == 'AM' and hour == '12'):
        return f"00{s[2:-2]}"
    elif period == "PM" and not hour == '12':
        hour = int(hour) + 12

    return f"{hour}{s[2:-2]}"

s = input()
result = timeConversion(s)
print(result)
