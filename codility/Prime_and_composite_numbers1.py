import math
def solution(N):
    cnt = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i == N // i:
                cnt += 1
            else:
                cnt += 2

    return cnt

# 시간복잡도 O(sqrt(N))

# https://app.codility.com/demo/results/trainingMX5EAX-K99/
