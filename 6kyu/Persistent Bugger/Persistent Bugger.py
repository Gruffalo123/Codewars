def persistence(n):
    count = 0
    while len(str(n)) >1:
        total = 1
        for item in str(n):
           total *= int(item)
        n = total
        count += 1
    return count

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))