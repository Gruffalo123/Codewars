def unique_in_order(iterable):
    li = []
    for item in iterable:
        if item not in li or li[-1] != item:
            li.append(item)
    return li


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
