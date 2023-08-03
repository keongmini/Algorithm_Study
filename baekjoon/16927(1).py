from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(min(N, M) // 2):
    nums = deque()

    x = i
    y = i
    nums.append(graph[x][y])

    for a, b in move:
        while True:
            nx = x + a
            ny = y + b

            if nx < i or nx >= N - i or ny < i or ny >= M - i:
                break

            if nx == i and ny == i:
                break

            nums.append(graph[nx][ny])
            x = nx
            y = ny

    for r in range(R % ((N - i * 2) * 2 + (M - i * 2) * 2 - 4)):
        nums.appendleft(nums.pop())

    x = i
    y = i
    graph[x][y] = nums.popleft()

    for a, b in move:
        while True:
            nx = x + a
            ny = y + b

            if nx < i or nx >= N - i or ny < i or ny >= M - i:
                break

            if nx == i and ny == i:
                break

            graph[nx][ny] = nums.popleft()
            x = nx
            y = ny


for i in range(N):
    for j in range(M):
        print(graph[i][j], end=" ")
    print()