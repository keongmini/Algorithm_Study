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