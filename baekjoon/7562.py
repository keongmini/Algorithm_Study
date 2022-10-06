import collections

N = int(input())

dir = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2))

for _ in range(N):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    x, y = map(int, input().split())
    nx, ny = map(int, input().split())

    if x == nx and y == ny:
        print(0)
        continue

    graph[x][y] = True
    q = collections.deque([(x, y, 0)])
    check = 0
    while q:
        nowx, nowy, cnt = q.popleft()

        for a, b in dir:
            if nowx + a < 0 or nowx + a >= I or nowy + b < 0 or nowy + b >= I or graph[nowx + a][nowy + b]:
                continue

            if nowx + a == nx and nowy + b == ny:
                print(cnt + 1)
                check = 1
                break

            graph[nowx + a][nowy + b] = True
            q.append((nowx + a, nowy + b, cnt + 1))

        if check == 1:
            break


