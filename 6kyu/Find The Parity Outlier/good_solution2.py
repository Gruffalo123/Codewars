def find_outlier(integers):
    listEven = []
    listOdd = []
    for i in integers:
        if i % 2 == 0:
            listEven.append(i)
        else:
            listOdd.append(i)

    if len(listOdd) == 1:
    # if len(listEven) > len(listOdd):
        return listOdd[0]
    else:
        return listEven[0]

li = [2, 4, 0, 100, 4, 11, 2602, 36]
li1 = [2, 4, 6, 8, 10, 3]
li2 = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(li))
print(find_outlier(li1))
print(find_outlier(li2))