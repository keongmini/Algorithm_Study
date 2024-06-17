A, B, C = map(int, input().split())

result = [0 for _ in range(100)]

for _ in range(3):
    a, b = map(int, input().split())

    for i in range(a - 1, b - 1):           # 떠난 시간 제외하기
        result[i] += 1

answer = 0
for n in result:
    if n == 1:
        answer += A
    elif n == 2:
        answer += B * 2
    elif n == 3:
        answer += C * 3

print(answer)



