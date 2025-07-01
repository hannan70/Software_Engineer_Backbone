
def longestCommonPrefix(strs):

    prefix = ''
    strs.sort()
    first = strs[0]
    last = strs[-1]

    for i in range(len(first)):
        if first[i] != last[i]:
            return prefix
        else:
            prefix += first[i]

    return prefix


strs = ["", "b"]
print(longestCommonPrefix(strs))
