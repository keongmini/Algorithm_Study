import sys

input = sys.stdin.readline

graph = [[int(s) for s in input().split()] for _ in range(19)]

move = [(1, 1), (1, 0), (0, 1), (-1, 1)]

for i in range(19):
    for j in range(19):
        if graph[i][j] == 1 or graph[i][j] == 2:
            now = graph[i][j]

            for a, b in move:
                length = 0
                ni = i
                nj = j

                while 0 <= ni < 19 and 0 <= nj < 19 and graph[ni][nj] == now:       # 한쪽으로만 이어지기 때문에 한쪽으로 이동
                    length += 1
                    ni += a
                    nj += b

                if length == 5:
                    prev_i = i - a          # 이전에 이어지는 부분 없는지 체크 - 이어지면 오목 x
                    prev_j = j - b

                    if 0 <= prev_i < 19 and 0 <= prev_j < 19 and graph[prev_i][prev_j] == now:
                        pass
                    else:
                        print(now)
                        print(i + 1, j + 1)
                        sys.exit(0)

print(0)
