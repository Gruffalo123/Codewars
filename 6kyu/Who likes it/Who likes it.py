def likes(names):
    string = " likes this"
    mul_str = " like this"
    if len(names) == 0:
        return 'no one'+string
    elif len(names) == 1:
        return names[0] + string
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + mul_str
    elif len(names) == 3:
        return ', '.join(names[0:2]) + ' and ' + names[2] + mul_str
    else:
        return ', '.join(names[0:2]) + ' and %s others' % (len(names)-2) + mul_str


print(likes([]))
print(likes(['a']))
print(likes(['a', 'b', 'v']))
print(likes(['a', 'b', 'v', 'f', 'g']))