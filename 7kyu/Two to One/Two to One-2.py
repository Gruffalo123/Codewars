def longest(str1,str2):
    str0 = str1 + str2
    s = set(str0)
    s1 = sorted(s)
    # print(s1)
    s2 = ''
    for k in s1:
        s2 += k
    print(s2, type(s2))


if __name__ == '__main__':
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    longest(a,b)
if __name__ == '__main__':
    a = "abcdefghijklmnopqrstuvwxyz"
    longest(a,a)