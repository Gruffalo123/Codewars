def spin_words(sentence):

    li = sentence.split(' ')

    for index,item in enumerate(li):
        if len(item) >= 5:
            li[index] = item[::-1]

    return ' '.join(li)


print(spin_words("welcome"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))