from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        visited = [[False for _ in range(M)] for i in range(N)]
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for a, b in move:
                    nx = x + a
                    ny = y + b

                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    
                    if visited[nx][ny] or grid[nx][ny] != "1":
                        continue
                    
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
        
        result = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    result += 1
        
        return result
