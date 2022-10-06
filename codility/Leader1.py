import collections

def solution(A):
    if not A:
        return -1

    graph = collections.defaultdict(list)
    cnt = collections.defaultdict(int)
    maxNum = 0
    maxIdx = ''
    for a in range(len(A)):
        graph[A[a]].append(a)
        cnt[A[a]] += 1
        if maxNum < cnt[A[a]]:
            maxIdx = A[a]
            maxNum = cnt[A[a]]

    check = [n for n in cnt.values() if n > len(A) // 2]

    if len(check) != 1:
        return -1

    return graph[maxIdx][0]

# 시간복잡도 O(N*log(N)) or O(N)

# https://app.codility.com/demo/results/training4NNKPS-BUH/