# dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 해당 위치의 주변 탐색
            dfs(i + 1, j) # 위
            dfs(i - 1, j) # 아래
            dfs(i, j + 1) # 우
            dfs(i, j - 1) # 좌

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


from collections import deque


# bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N = len(grid)
        M = len(grid[0])

        visited = [[False for _ in range(M)] for i in range(N)]

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True

            while q:
                a, b = q.popleft()

                for i, j in move:
                    na = a + i
                    nb = b + j

                    if na < 0 or na >= N or nb < 0 or nb >= M:
                        continue

                    if grid[na][nb] == "0" or visited[na][nb]:
                        continue

                    visited[na][nb] = True
                    q.append((na, nb))

        result = 0
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    result += 1

        return result