import heapq
T = int(input())

INF = 1e9

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(d, i, j):
    q = []

    heapq.heappush(q, (d, i, j))
    distance[i][j] = d

    while q:
        now, a, b = heapq.heappop(q)

        if distance[a][b] < now:
            continue

        for x, y in move:
            dx = a + x
            dy = b + y

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            cost = now + graph[dx][dy]

            if cost < distance[dx][dy]:
                distance[dx][dy] = cost
                heapq.heappush(q, (cost, dx, dy))


for _ in range(T):
    N = int(input())

    graph = []
    for _ in range(N):
        new = list(map(int, input().split()))
        graph.append(new)

    distance = [[INF] * N for _ in range(N)]

    dijkstra(graph[0][0], 0, 0)

    print(distance[N - 1][N - 1])
