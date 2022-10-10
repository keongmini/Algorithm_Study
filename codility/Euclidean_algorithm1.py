# Timeour Error
# 시간복잡도 O(N + M)

def solution(N, M):
    visited = [False for _ in range(N)]
    cnt = 0

    idx = 0
    while not visited[idx]:
        visited[idx] = True
        cnt += 1

        idx = idx + M
        if idx >= N:
            idx = idx % N

    return cnt


# 유클리드 호제법 - 최대공약수 구하기
import math
def solution(N, M):
    gcd = math.gcd(N, M)

    return N // gcd

# O(log(N + M))

# https://app.codility.com/demo/results/trainingGPMW7Z-GAT/