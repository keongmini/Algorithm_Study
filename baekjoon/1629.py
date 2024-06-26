# 지수법칙 : a^(n+m) = a^n * a^m
# 모듈러 성질 : (a*b)%c = (a%c * b%c)%c

def check(a, b, c):
    if b == 1:
        return a % c

    n = check(a, b // 2, c)

    if b % 2 == 0:
        return n * n % c
    else:
        return a * n * n % c

A, B, C = map(int, input().split())
print(check(A, B, C))

# -------------------------------------------------------
# print(pow(A, B, C))     # pow: A의 B 거듭제곱을 구해서 C로 나눈 값


