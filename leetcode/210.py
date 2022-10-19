# leetcode discuss answer
class Solution:
    def findOrder(self, N, P):
        G, indegree, ans = defaultdict(list), [0] * N, []       # 선수과목 기준으로 저장 dict, 선수과목 개수(인덱스별), 답 저장 리스트
        for nxt, pre in P:
            G[pre].append(nxt)
            indegree[nxt] += 1

        def dfs(cur):
            ans.append(cur)     # 답 저장
            indegree[cur] = -1      # -1 일 경우 처리 완료임
            for nextCourse in G[cur]:       # 해당 과목이 선수과목인 과목 처리
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    dfs(nextCourse)

        for i in range(N):
            if indegree[i] == 0:
                dfs(i)

        return ans if len(ans) == N else []

# 위상정렬
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