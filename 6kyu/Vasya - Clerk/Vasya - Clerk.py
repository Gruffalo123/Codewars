def tickets(people):
    n25 = n50 = n100 = 0
    for i in people:
        if i == 25:
            n25 += 1
        elif i == 50:
            n25 -= 1
            n50 += 1
        elif i == 100 and n50 > 0:
            n50 -= 1
            n25 -= 1
        elif i == 100 and n50 == 0:
            n25 -= 3
        if n25 < 0 or n50 < 0:
            return 'NO'

    return 'YES'


print(tickets([25, 25, 50]))
print(tickets([25, 100]))