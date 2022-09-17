class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # bfs 풀이
        def bfs(path, start):
            q = collections.deque([start])
            visited[start] = True

            while q:
                now = q.popleft()

                if destination in path[now]:
                    return True

                for num in path[now]:
                    if not visited[num]:
                        visited[num] = True
                        q.append(num)

            return False

        if n == 1:
            return True

        path = [[] for i in range(n)]
        for edge in edges:
            path[edge[0]].append(edge[1])
            path[edge[1]].append(edge[0])

        visited = [False] * n

        return bfs(path, source)

        # --------------------------------------------------------------
        # dfs 풀이
        def dfs(path, start, visited):
            if destination in path[start]:
                return True

            for i in range(len(path[start])):
                if not visited[start][i]:
                    visited[start][i] = True
                    if dfs(path, path[start][i], visited):
                        return True

            return False

        if n == 1:
            return True

        path = [[] for i in range(n)]
        for edge in edges:
            path[edge[0]].append(edge[1])
            path[edge[1]].append(edge[0])

        visited = []
        for i in range(n):
            visited.append([False] * len(path[i]))

        return dfs(path, source, visited)



