def series_sum(n):
    # Happy Coding ^_^
    sum = 0
    for i in range(0, n):
        sum = sum + 1 / (1 + 3 * i)

    return '%.2f' % sum

if __name__ == '__main__':
    print(series_sum(1))
    print(series_sum(2))
    print(series_sum(3))