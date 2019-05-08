def dig_pow(n, p):
    count = 0
    for i,item in enumerate(str(n)):
        count += int(item) ** (p+i)

    d = count/n
    # %  和  /
    return d if count%n == 0 else -1

    # d1 = str(d).split('.')
    # if int(d1[1]) == 0:
    #     return int(d1[0])
    # else:
    #     return -1

# def dig_pow(n, p):
#   s = 0
#   for i,c in enumerate(str(n)):
#      s += pow(int(c),p+i)
#   return s/n if s%n==0 else -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))


