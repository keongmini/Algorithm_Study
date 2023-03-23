def solution(s):
    index = {}

    result = []

    for i, char in enumerate(s):
        if char not in index:
            result.append(-1)
            index[char] = i
        else:
            result.append(i - index[char])
            index[char] = i

    return result