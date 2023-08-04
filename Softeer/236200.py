import sys

K, P, N = map(int, input().split())

for n in range(N):
    K = (K * P) % 1000000007

print(K)


# 오답
# import sys
#
# K, P, N = map(int, input().split())
#
# result = K * (P ** N)
#
# print(result % 1000000007)