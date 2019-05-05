def find_outlier(integers):
    # 列表内奇数数目的和
    odd_count = 0

    # 列表内偶数数目的和
    even_count = 0

    for i in integers:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count > even_count:
        for j in integers:
            if j % 2 == 0:
                return j
    else:
        for j in integers:
            if j % 2 == 1:
                return j


li = [2, 4, 0, 100, 4, 11, 2602, 36]
li1 = [2, 4, 6, 8, 10, 3]
li2 = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(li))
print(find_outlier(li1))
print(find_outlier(li2))