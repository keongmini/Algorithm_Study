import heapq

T = int(input())

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dijkstra(d, i, j):
    q = []

    heapq.heappush(q, (d, i, j))
    distance[i][j] = d

    while q:
        n, a, b = heapq.heappop(q)

        if distance[a][b] < n:
            continue

        for x, y in move:
            dx = a + x
            dy = b + y
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            cost = n + graph[dx][dy]

            if cost < distance[dx][dy]:
                distance[dx][dy] = cost
                heapq.heappush(q, (cost, dx, dy))

for _ in range(T):
    N = int(input())
    graph = []
    for _ in range(N):
        new = list(map(int, input().split()))
        graph.append(new)

    distance = [[1e9] * (N + 1) for _ in range(N + 1)]

    dijkstra(graph[0][0], 0, 0)

    print(distance[N - 1][N - 1], end=" ")

