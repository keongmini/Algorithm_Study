# 내 풀이
from collections import deque

n, m = map(int, input().split())
balls = deque(map(int, input().split()))

result = 0
while balls:
    now = balls.popleft()

    for i in range(len(balls)):
        if now != balls[i]:
            result += 1

print(result)

# 책 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11        # 최대 무게 10 -> 1부터 10까지 담을 리스트 (0 제외)

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)

# 내 풀이와 책 풀이가 구현하고자 한 방식은 동일
# 내 풀이는 리스트에서 하나씩 제거하면서 남은 무게 중 다른 것을 확인하여 하나씩 증가 하는 방식
# 책 풀이는 무게의 개수를 리스트에 저장 -> 해당 무게 개수 빼기 -> 남은 개수와 곱하여 증가하는 방식


