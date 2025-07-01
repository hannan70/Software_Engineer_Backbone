
def removeDuplicateLetters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    stack = []
    visited = set()

    for char in s:
        char_count[char] -= 1
        print(char_count)
        if char in visited:
            continue
        else:
            while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                removed_char = stack.pop()
                visited.remove(removed_char)


        stack.append(char)
        visited.add(char)

    return "".join(stack)

s = "cbacdcbc"
result = removeDuplicateLetters(s)
print(result)

