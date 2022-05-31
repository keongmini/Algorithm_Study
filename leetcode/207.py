# dfs 풀이 - 순환구조만 고려 => Time Limit Exceeded
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

# 효율성 고려한 풀이(순환 구조, 복잡한 구조 모두 불필요한 탐색 막기)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
