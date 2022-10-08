import collections

n = int(input())

def bfs(a, b, visited):
    q = collections.deque([(a, b)])

    while q:
        now = q.popleft()

        if abs(dx - now[0]) + abs(dy - now[1]) <= 1000:
            return 'happy'

        for n in range(con):
            if not visited[n]:
                nx, ny = conList[n]
                if abs(nx - now[0]) + abs(ny - now[1]) <= 1000:         # 현재 위치와 거리가 가능한 것만 확인 
                    q.append((nx, ny))
                    visited[n] = True

    return 'sad'


for _ in range(n):
    con = int(input())
    conList = []

    x, y = map(int, input().split())

    for _ in range(con):
        conList.append(list(map(int, input().split())))

    visited = [False] * (con)

    dx, dy = map(int, input().split())

    print(bfs(x, y, visited))

