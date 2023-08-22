N = int(input())

graph = [[s for s in input()] for _ in range(N)]

result = 0


def check():
    global result

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if graph[i][j] == graph[i][j - 1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if graph[i][j] == graph[i - 1][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1


move = [(1, 0), (0, 1)]

for i in range(N):
    for j in range(N):

        for a, b in move:
            nx = i + a
            ny = j + b

            if nx >= N or ny >= N:
                continue

            graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]
            check()
            graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]

print(result)