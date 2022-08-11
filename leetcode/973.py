class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            d = x ** 2 + y ** 2
            heapq.heappush(heap, (d, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result

# 힙 사용 하는 이유: 같은 거리를 갖는 경우 더 순서가 빠른(더 가까운) 값이 출력되어야 하기 때문에 
