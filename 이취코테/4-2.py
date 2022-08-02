n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)

# 00시 00분 00초 부터 23시 59분 59초 까지 해도 경우의수가 86400개 < 100000 이므로 삼중반복문 사용가능