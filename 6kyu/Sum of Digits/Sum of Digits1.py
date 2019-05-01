def digital_root(n):
    sum = 0
    while len(str(n))>1:
        for i in str(n):
            sum += int(i)
        n = sum
        sum = 0

    else:
        sum = n
    return sum

if __name__ == '__main__':
    print(digital_root(7))
    print(digital_root(16))
    print(digital_root(256))
    print(digital_root(132189))