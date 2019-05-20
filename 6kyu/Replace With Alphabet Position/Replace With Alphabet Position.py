def alphabet_position(text):
    li = []
    for item in text:
        if item.isalpha():
            # join方法不能对int数据类型使用，需要转换成字符串
            li.append(str(ord(item.lower())-96))
            # li.append(str(ord(item.upper())-64))
    return ' '.join(li)


print(alphabet_position("The sunset sets at twelve o' clock."))