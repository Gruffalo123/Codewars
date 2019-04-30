def longest(str1,str2):
    list1,list2 = [],[]

    for i in str1:
        list1.append(i)
    for j in str2:
        list2.append(j)

    list = list1 + list2

    s = set(list)
    s1 = sorted(s)

    s2 = ''
    for k in s1:
        s2 += k
    print(s2,type(s2))

if __name__ == '__main__':
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    longest(a,b)
if __name__ == '__main__':
    a = "abcdefghijklmnopqrstuvwxyz"
    longest(a,a)

