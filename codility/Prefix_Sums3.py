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