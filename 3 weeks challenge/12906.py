def solution(arr):
    result = []

    prev = -1

    for a in arr:
        if a != prev:
            result.append(a)
            prev = a

    return result