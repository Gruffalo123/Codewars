def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


if __name__ == '__main__':
    print(series_sum(1))
    print(series_sum(2))
    print(series_sum(3))