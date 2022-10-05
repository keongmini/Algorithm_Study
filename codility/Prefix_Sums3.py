# Timeout Error
# 시간 복잡도 O(N * M)
def solution(S, P, Q):
    N = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    if set(S) == 1:
        return [N[S[0]]] * len(P)

    if not P:
        return []

    result = [4 for _ in range(len(P))]
    for i in range(len(P)):
        if Q[i] - P[i] == len(S):
            result[i] = 1
            continue

        now = list(S[P[i]:Q[i] + 1])
        now.sort()
        result[i] = N[now[0]]

    return result


def solution(S, P, Q):
    N = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    result = []
    for i in range(len(P)):
        for s in N:
            if s in S[P[i]: Q[i] + 1]:
                result.append(N[s])
                break

    return result


def solution(S, P, Q):
    N = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    result = []
    for i in range(len(P)):
        minNum = 4
        nums = set(S[P[i]: Q[i] + 1])
        for n in nums:
           minNum = min(minNum, N[n])
        result.append(minNum)

    return result

# O(N + M)
def solution(S, P, Q):
    N = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    result = []
    for i in range(len(P)):
        char = S[P[i]: Q[i] + 1]
        for s in N:
            if s in char:
                result.append(N[s])
                break
    return result


def solution(S, P, Q):
    N = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    result = []
    for i in range(len(P)):
        char = S[P[i]: Q[i] + 1]
        if 'A' in char:
            num = 1
        elif 'C' in char:
            num = 2
        elif 'G' in char:
            num = 3
        elif 'T' in char:
            num = 4

        result.append(num)

    return result