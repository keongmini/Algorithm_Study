# Timeout error
# 시간복잡도 O(N * log(log(N)) + M * N) or O(M * N**3) or O(M * N ** (3/2))
def check(N):
    result = [False for _ in range(N + 1)]

    for i in range(2, int(N ** 0.5) + 1):
        if not result[i]:
            for j in range(i * i, N + 1, i):
                result[j] = True

    return result


def solution(N, P, Q):
    prime_ = check(N)
    prime = [n for n in range(2, N + 1) if not prime_[n]]
    semiprime = [False for _ in range(N + 1)]

    for i in prime:
        for j in prime:
            if i * j <= N and not semiprime[i * j]:
                semiprime[i * j] = 1

    result = []
    for i in range(len(P)):
        tmp = semiprime[P[i]: Q[i] + 1].count(1)
        result.append(tmp)

    return result


# 통과
def solution(N, P, Q):
    check = [False for _ in range(N + 1)]
    prime = []

    for i in range(2, N + 1):
        if not check[i]:
            prime.append(i)
            for j in range(i * i, N + 1, i):
                check[j] = True

    semiprime = [0 for _ in range(N + 1)]

    for i in prime:
        for j in prime:
            if i * j > N:           # 안해주면 timeout error 발생 
                break

            if not semiprime[i * j]:
                semiprime[i * j] = 1

    for i in range(1, N + 1):
        semiprime[i] += semiprime[i - 1]

    answer = []
    for i in range(len(P)):
        answer.append(semiprime[Q[i]] - semiprime[P[i] - 1])

    return answer

# 시간 복잡도 O(N * log(log(N)) + M)

# https://app.codility.com/demo/results/trainingJEM7NZ-VM6/
