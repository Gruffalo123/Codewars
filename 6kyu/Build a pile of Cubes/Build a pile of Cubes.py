def find_nb(m):
    count = 0
    n = 0
    while count < m:
        n += 1
        count += n ** 3
    if count == m:
        return n
    else:
        return -1


print(find_nb(4183059834009))
print(find_nb(24723578342962))
print(find_nb(135440716410000))