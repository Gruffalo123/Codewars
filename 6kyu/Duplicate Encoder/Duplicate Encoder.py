def duplicate_encode(word):
    li = []
    for item in word.lower():
        if word.lower().count(item) > 1:
            li.append(")")
        else:
            li.append("(")
    return ''.join(li)


print(duplicate_encode('din'))
print(duplicate_encode('recede'))
print(duplicate_encode('Success'))
print(duplicate_encode('(( @'))