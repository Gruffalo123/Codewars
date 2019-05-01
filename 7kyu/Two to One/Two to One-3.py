def longest(str1,str2):
    return ''.join(sorted(set(str1+str2)))


if __name__ == '__main__':
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    print(longest(a,b))
if __name__ == '__main__':
    a = "abcdefghijklmnopqrstuvwxyz"
    print(longest(a,a))