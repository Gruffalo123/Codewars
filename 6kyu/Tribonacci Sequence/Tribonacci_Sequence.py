def tribonacci(signature, n):
    # if n == 0:
    #     return []

    if n < len(signature):
        return signature[:n]

    # while len(signature) < n:#10
    else:
        for i in range(n-3):#最后一次：6,7,8,n=10,i=4,5,6
            signature.append(signature[i]+signature[i+1]+signature[i+2])
    return signature

print(tribonacci([1,1,1],10))
print(tribonacci([1,1,1],0))
print(tribonacci([1,1,1],1))
print(tribonacci([1,3,5],2))