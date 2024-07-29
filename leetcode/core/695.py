from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def check(x, y):
            q = deque()
            q.append((x, y))
            cnt = 1

            while q:
                a, b = q.popleft()

                for i, j in move:
                    na = a + i
                    nb = b + j

                    if na < 0 or na >= len(grid) or nb < 0 or nb >= len(grid[0]):
                        continue

                    if grid[na][nb] == 0:
                        continue

                    grid[na][nb] = 0
                    q.append((na, nb))
                    cnt += 1

            return cnt

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    result = max(result, check(i, j))

        return result
# 시간 복잡도 O(n * m) 이중 반복문
# 공간 복잡도 O(n * m) 최악의 경우 grid의 모든 값 저장

s = Solution()
s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])