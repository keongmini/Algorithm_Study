# dfs 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]


# 스택 연산 dfs 풀이
# pop(0) -> O(n) / pop() -> O(1)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]



