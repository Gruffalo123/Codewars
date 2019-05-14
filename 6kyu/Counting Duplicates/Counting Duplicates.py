def duplicate_count(text):
    count = 0
    li = []
    for item in text:
        if item.isalpha():
            li.append(item.lower())
        elif item.isdigit():
            li.append(item)
# set 不去重的话每次遍历相同元素都会加一
    for i in set(li):
        if li.count(i) > 1:
            count += 1
    return count


print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("ABBA"))
print(duplicate_count("aA11"))