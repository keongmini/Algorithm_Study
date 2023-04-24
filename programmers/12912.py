def solution(a, b):
    if a > b:
        a, b = b, a

    result = 0
    for i in range(a, b + 1):
        result += i

    return result