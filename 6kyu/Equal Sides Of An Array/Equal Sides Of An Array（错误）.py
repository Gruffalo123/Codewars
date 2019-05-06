# wrong answer
# 我自己做错的思路想法。。
# 用元素做判断会引发相等元素值的冲突
# 以下是错误解法、错误、错误。
# 所以测试返回值错误 -1


def find_even_index(arr):
    flag = True
    while flag:
        for item in arr:
            if sum(arr[:arr.index(item)]) == sum(arr[arr.index(item)+1:]):
                return arr.index(item)

            if arr.index(item) == len(arr)-1:
                flag = False
                return -1

li = [20,10,30,10,10,15,35]
print(find_even_index(li))

