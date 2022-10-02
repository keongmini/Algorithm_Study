from collections import deque

N = int(input())

apple = []
for _ in range(int(input())):
    apple.append(list(map(int, input().split())))

direction = {}
for _ in range(int(input())):
    sec, order = input().split()
    direction[int(sec)] = order

d = [(0,1), (1, 0), (0, -1), (-1, 0)]

x = 1
y = 1

result = 0
idx = 0
q = deque([[x, y]])
while True:
    result += 1
    x += d[idx][0]
    y += d[idx][1]

    if x < 1 or x > N or y < 1 or y > N or [x, y] in q:
         print(result)
         break

    if [x, y] not in apple:
        q.popleft()
    else:                                       # 주의!! 놓치기 쉬운 부분 - 한번 먹은 사과는 다시 먹을 수 없음!
        apple.remove([x,y])

    q.append([x, y])

    if result in direction:
        if direction[result] == 'D':
            idx = (idx + 1) % 4
        else:
            idx = (idx - 1) % 4

