def countBits(n):
    bins = bin(n)
    count = 0
    for i in str(bins):
        if i == '1':
            count += 1
    return count


print(countBits(0))
print(countBits(4))
print(countBits(7))
print(countBits(9))
print(countBits(10))