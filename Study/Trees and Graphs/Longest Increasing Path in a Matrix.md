# leetcode 329. [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) (hard)

* 문제 해설 : 행렬 내에 어떤 값부터 시작해서 계속 증가하는 값으로 이동할 때 이동할 수 있는 최대 거리 구하기  
 
  example 1. 
  ```text
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
    ```
  <img src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" />
  
  example 2.
  ```text
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
    ```
  <img src="https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg"/>
  
  example 3.
  ```text
    Input: matrix = [[1]]
    Output: 1
    ```
  
  제약조건.
  ```text
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1
    ```
  
* 문제 접근 방법
  행렬내에 값별로 위치를 저장(딕셔너리), 작은 값부터 dfs로 탐색해서 최대길이 갱신, 행렬 내에 최대값과 현재 행렬 값의 차가 최대길이 보다 작으면 탐색 중지(최대길이보다 더 긴 이동거리가 나올 수 없기 때문에) 
  -> 시간초과 
  
* solution 풀이 
  - dfs + 메모이제이션  
    참고. [discussion python solution](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms)
    
    dfs로 탐색하되 이미 방문한 위치의 최대거리가 저장되어있으면 시작 위치부터 방문한 위치 거리 + 방문한 위치의 최대거리 해주면 됨 -> 메모이제이션 사용  
    -> 이중탐색 방지 
    
    주의사항! 처음 dfs 돌릴 때 비교하는 vlaue값을 -1로 설정하여야 첫 값부터 시작할 수 있음  
    (처음 value값을 해당 행렬의 값으로 넘기면 종료조건에 걸려서 돌아가지 않음)
    
    **시간복잡도 O(MxN)**
    
    ```python
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
            dp = [[0]* N for i in range(M)]     # 메모이제이션 구현
            
            result = []
            for x in range(M):
                for y in range(N):
                    result.append(dfs(x, y, -1))
            
            return max(result)
    ```