n, m = map(int, input().split())
cnt = 0

# # 1. 단순 풀이
# while n > 1:
#     cnt += 1
#
#     if n % m == 0:
#         n /= m
#     else:
#         n -= 1
#
# print(cnt)

# 2. 효율적인 풀이
result = 0

while True:
    target = (n // m) * m
    result += (n - target)
    n = target
    if n < m:
        break

    result += 1
    n //= m

result += (n - 1)
print(result)
