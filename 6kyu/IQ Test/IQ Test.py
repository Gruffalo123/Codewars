def iq_test(numbers):
    li = [i for i in numbers.split()]
    odd = []
    even = []
    for item in li:
        if int(item) % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    if len(odd) == 1:
        return li.index(odd[0])+1
    else:
        return li.index(even[0])+1


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))