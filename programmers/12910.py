def solution(arr, divisor):
    result = []

    for a in arr:
        if a % divisor == 0:
            result.append(a)

    result.sort()

    if not result:
        result.append(-1)

    return result