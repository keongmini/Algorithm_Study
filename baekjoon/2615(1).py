import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(19)]

move = [(1, 0), (0, 1), (1, 1), (-1, 1)]


for i in range(19):
    for j in range(19):
        if graph[i][j] == 1 or graph[i][j] == 2:
            now = graph[i][j]

            for a, b in move:
                ni = i
                nj = j
                cnt = 0

                while 0 <= ni < 19 and 0 <= nj < 19 and graph[ni][nj] == now:
                    cnt += 1
                    ni += a
                    nj += b

                if cnt == 5:
                    prev_i = i - a
                    prev_j = j - b

                    if 0 <= prev_i < 19 and 0 <= prev_j < 19 and graph[prev_i][prev_j] == now:
                        pass
                    else:
                        print(now)
                        print(i + 1, j + 1)
                        sys.exit(0)

print(0)