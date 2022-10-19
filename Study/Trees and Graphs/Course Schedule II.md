# leetcode 210. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (medium)

* 문제 해설 : 과목 수와 과목별 선수강 과목이 주어짐, 선수강 과목을 수강해야 그 다음 과목을 수강할 수 있음, 어떤 순서로 강의를 수강해야 강의를 모두 수강할 수 있을지 강의 리스트 출력, 만약 불가능할 경우 빈 배열 출력

  example 1.
  ```text
  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: [0,1]
  Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
  ```
  
  example 2. 
  ```text
  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0,2,1,3]
  Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
  So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
  ```
  
  example 3.
  ```text
  Input: numCourses = 1, prerequisites = []
  Output: [0]
  ```
  
  제약조건.
  ```text
  1 <= numCourses <= 2000
  0 <= prerequisites.length <= numCourses * (numCourses - 1)
  prerequisites[i].length == 2
  0 <= ai, bi < numCourses
  ai != bi
  All the pairs [ai, bi] are distinct.
  ```
  
* 문제 접근 방법  
  선수강과목(key)과 다음 과목(value)을 딕셔너리에 저장  
  가장 첫번째로 수강해야 하는 과목을 루트라고 생각하고 bfs를 돌면서 과목을 방문처리하면서 돌리려고 함  
  가장 첫번째 과목이 어떤 과목인지 찾는 과정 구현 x, 이미 방문처리가 되어 해당 과목과 연결되어있는 다른 과목 방문 불가 등의 문제로 구현 x  

* solution 풀이 
  - dfs
    1. 선수강 과목을 기준으로 다음 수강과목을 모두 저장(딕셔너리), 과목별 선수강 과목 갯수 저장(딕셔너리)
    1. 선수강 과목이 없는 과목부터 dfs 시작 -> 해당 과목이 선수강 과목인 과목으로 연결하여 탐색
    
    **시간복잡도 O(M + N)** M은 연결된 갯수, N은 과목수 
    
    ```python
    from collections import defaultdict
    class Solution:
        def findOrder(self, N, P):
            G, indegree, ans = defaultdict(list), [0] * N, []  
            for nxt, pre in P:
                G[pre].append(nxt)
                indegree[nxt] += 1
    
            def dfs(cur):
                ans.append(cur)  
                indegree[cur] = -1
                for nextCourse in G[cur]: 
                    indegree[nextCourse] -= 1
                    if indegree[nextCourse] == 0:
                        dfs(nextCourse)
    
            for i in range(N):
                if indegree[i] == 0:
                    dfs(i)
    
            return ans if len(ans) == N else []
    ```
    
  - 위상정렬 
    
    참고. [위상정렬](https://github.com/keongmini/Today-I-Learned/blob/master/Algorithm/Topological%20Sort.md)
    
    **시간복잡도 O(M + N)** M은 연결된 갯수, N은 과목수 
  
    ```python
    from collections import defaultdict, deque
    class Solution:
        def findOrder(self, numCourses, prerequisites):
            adj_list = defaultdict(list)
            indegree = {}
            for dest, src in prerequisites:
                adj_list[src].append(dest)
                indegree[dest] = indegree.get(dest, 0) + 1
    
            zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
    
            topological_sorted_order = []
    
            while zero_indegree_queue:
                vertex = zero_indegree_queue.popleft()
                topological_sorted_order.append(vertex)
    
                if vertex in adj_list:
                    for neighbor in adj_list[vertex]:
                        indegree[neighbor] -= 1
    
                        if indegree[neighbor] == 0:
                            zero_indegree_queue.append(neighbor)
    
            return topological_sorted_order if len(topological_sorted_order) == numCourses else []
    ```