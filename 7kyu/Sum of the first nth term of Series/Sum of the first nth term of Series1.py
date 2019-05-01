def series_sum(n):
    # Happy Coding ^_^
    if n == 0:
        sum = 0
    else:
        sum = 1
        if n > 1:
            for i in range(2, n + 1):
                sum = sum + 1 / (1 + 3 * (i - 1))

    return '%.2f' % sum
    #round函数不行

if __name__ == '__main__':
    print(series_sum(1))
    print(series_sum(2))
    print(series_sum(3))
