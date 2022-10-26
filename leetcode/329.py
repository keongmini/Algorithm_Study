# dfs로만 풀이 - 시간초과
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    visited = [[False for _ in range(len(matrix[0]))] for i in range(len(matrix))]
    nums = collections.defaultdict(list)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            nums[matrix[i][j]].append((i, j))

    result = 0

    def dfs(x, y, cnt, p):
        nonlocal result
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            result = max(result, cnt - 1)
            return

        if (matrix[x][y] <= p and cnt != 1) or (visited[x][y] and matrix[x][y] == p):
            result = max(result, cnt - 1)
            return

        visited[x][y] = True

        dfs(x + 1, y, cnt + 1, matrix[x][y])
        dfs(x - 1, y, cnt + 1, matrix[x][y])
        dfs(x, y + 1, cnt + 1, matrix[x][y])
        dfs(x, y - 1, cnt + 1, matrix[x][y])


    lines = sorted(nums.keys())
    maxNum = lines[-1]

    for line in lines:
        if maxNum - line < result:
            return result

        for a, b in nums[line]:
            if not visited[a][b]:
                dfs(a, b, 1, line)

    return result

# dfs + dp - 통과 
class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j, value):
            if i < 0 or i >= M or j < 0 or j >= N or matrix[i][j] <= value:
                return 0

            v = matrix[i][j]

            if not dp[i][j]:
                left = dfs(i, j - 1, v)
                right = dfs(i, j + 1, v)
                up = dfs(i - 1, j, v)
                down = dfs(i + 1, j, v)

                dp[i][j] = 1 + max(left, right, up, down)

            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]  # 메모이제이션 구현

        result = []
        for x in range(M):
            for y in range(N):
                result.append(dfs(x, y, -1))

        return max(result)