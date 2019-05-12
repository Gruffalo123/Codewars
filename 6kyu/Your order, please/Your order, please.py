def order(sentence):
    li1 = []
    li = [item for item in sentence.split(' ')]
    for i in li:
        li1.append(i)
    # li1 = li # Error 这样内存地址还是一样的，li改变则li1也改变

    for item in li:
        for i in item:
            for j in range(10):
                if i == str(j):
                    li1[j-1] = item

    return ' '.join(li1)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))