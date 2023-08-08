N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    graph[i][0] = graph[i][0] + min(graph[i - 1][1], graph[i - 1][2])
    graph[i][1] = graph[i][1] + min(graph[i - 1][0], graph[i - 1][2])
    graph[i][2] = graph[i][2] + min(graph[i - 1][0], graph[i - 1][1])

print(min(graph[N - 1]))