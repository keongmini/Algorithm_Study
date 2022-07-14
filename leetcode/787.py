# Time Limit Exceeded
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        Q = [(0, src, k)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))

        return -1

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in flights:
            graph[u].append([v, w])

        visit = {}
        Q = [(0, src, 0)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if node not in visit or visit[node] > k:
                visit[node] = k
                for v, w in graph[node]:
                    if k <= K:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))

        return -1