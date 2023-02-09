def solution(array, commands):
    result = []

    for i, j, k in commands:
        tmp = array[i - 1: j]
        tmp.sort()
        result.append(tmp[k - 1])

    return result