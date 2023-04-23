def solution(arr):
    result = []

    prev = -1

    for i in arr:
        if i != prev:
            result.append(i)
            prev = i

    return result