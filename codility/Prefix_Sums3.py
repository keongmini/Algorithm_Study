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

# 87%
# set 보다 string 값에서 찾는 게 빠름
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

# 통과
def solution(S, P, Q):
    A, C, G, T = 0, 0, 0, 0
    now = [(0, 0, 0, 0)]
    for s in S:
        if s == 'A':
            A += 1
        elif s == 'C':
            C += 1
        elif s == 'G':
            G += 1
        elif s == 'T':
            T += 1

        now.append((A, C, G, T))        # char 순서대로 현재 갯수 모두 저장

    dna = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for p, q in zip(P, Q):
        nowP, nowQ = now[p], now[q + 1]     # 달라진 값 비교

        if nowP[0] != nowQ[0]:
            result.append(1)
        elif nowP[1] != nowQ[1]:
            result.append(2)
        elif nowP[2] != nowQ[2]:
            result.append(3)
        elif nowP[3] != nowQ[3]:
            result.append(4)
        else:
            result.append(dna[S[p]])

    return result

# 시간 복잡도 O(N + M)

# https://app.codility.com/demo/results/trainingY8AGX4-X5V/