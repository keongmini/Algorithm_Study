

# python3 시간초과 / pypy3 통과
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = []

for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

for _ in range(R):
    for i in range(min(N, M) // 2):     # 가로, 세로 중 길이가 작은 것
        x = i
        y = i
        prev = graph[x][y]          # 저장해둘 값

        # 좌
        for j in range(i + 1, N - i):
            next_value = graph[j][y]        # 그 다음 값을 미리 저장해두고
            graph[j][y] = prev              # 직전에 저장해둔 값 자리에 prev 값 넣기
            prev = next_value               # prev 값 갱신
            x = j                           # 현재 위치 어딘지 알기 위해 저장

        # 하
        for j in range(i + 1, M - i):
            next_value = graph[x][j]
            graph[x][j] = prev
            prev = next_value
            y = j

        # 우
        for j in range(N - i - 2, i - 1, -1):
            next_value = graph[j][y]
            graph[j][y] = prev
            prev = next_value
            x = j

        # 상
        for j in range(M - i - 2, i - 1, -1):
            next_value = graph[x][j]
            graph[x][j] = prev
            prev = next_value
            y = j

for n in range(N):
    for m in range(M):
        print(graph[n][m], end=' ')
    print()
