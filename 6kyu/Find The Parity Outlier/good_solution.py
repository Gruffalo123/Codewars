def find_outlier(integers):
    odds = [i for i in integers if i % 2 != 0]
    evens = [i for i in integers if i % 2 == 0]
    return odds[0] if len(evens) > len(odds) else evens[0]

li = [2, 4, 0, 100, 4, 11, 2602, 36]
li1 = [2, 4, 6, 8, 10, 3]
li2 = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(li))
print(find_outlier(li1))
print(find_outlier(li2))