def longest_consec(strarr, k):
    li = []
    if len(strarr) == 1 or k > len(strarr) or k <= 0:
        return ''
    for i in range(len(strarr) - k + 1):
        len_str = ''.join(strarr[i:i+k])
        li.append(len_str)
        
    # max函数的key参数
    return max(li, key=len)


x = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
print(longest_consec(x, 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))