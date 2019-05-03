def solution(number):
    count = 0
    for item in range(1, number):
        if item % 3 == 0 or item % 5 == 0:
            count += item
    return count

print(solution(10))
print(solution(0))
print(solution(125))