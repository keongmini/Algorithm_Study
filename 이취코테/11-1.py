# 내 풀이
n = int(input())    # 모험가 수

rate = list(map(int,input().split()))
rate.sort()

cnt = 0
while rate:
    idx = len(rate) - 1
    key = rate[idx]
    for i in range(key):
        rate.pop()
    cnt += 1

print(cnt)

# 책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# 내 풀이는 큰 숫자부터 확인 / 책 풀이는 작은 숫자부터 확인
# 책 풀이가 가능한 이유는 어처피 공포도를 넘지 못하면 그룹수가 증가되지 않기 때문에
