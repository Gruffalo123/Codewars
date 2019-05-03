def find_it(seq):
    # set_seq = set(seq)
    # for item in set_seq:
    for item in seq:
        if seq.count(item)%2 == 1:
            return item

li = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(li))
