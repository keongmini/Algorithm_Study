def solution(citations):
    citations.sort()

    hIndex = 0
    idx = 0
    for i in range(citations[-1]):
        if citations[idx] < i:
            idx += 1

        if len(citations[idx:]) >= i and len(citations[:idx]) <= i:
            hIndex = i

    return hIndex
