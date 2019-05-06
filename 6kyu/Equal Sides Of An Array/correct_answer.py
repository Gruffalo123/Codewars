def find_even_index(arr):
    for item in range(len(arr)):
        if sum(arr[:item]) == sum(arr[item+1:]):
            return item

    # 如果循环结束也没有找到符合条件的值
    return -1

if __name__ == '__main__':
    li = [20, 10, 30, 10, 10, 15, 35]
    print(find_even_index(li))