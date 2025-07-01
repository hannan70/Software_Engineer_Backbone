
numbers = int(input())
numberList = []
for i in range(numbers):
    items = input().split()
    if items[0] == 'insert':
        numberList.insert(int(items[1]), int(items[2]))
    elif items[0] == 'print':
        print(numberList)
    elif items[0] == 'remove':
        numberList.remove(int(items[1]))
    elif items[0] == 'append':
        numberList.append(int(items[1]))
    elif items[0] == 'pop':
        numberList.pop()
    elif items[0] == 'sort':
        numberList.sort()
    else:
        numberList.sort(reverse=True)

