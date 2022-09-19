class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # 좌표를 저장할 heap
        heap = [(0, 0)]

        # 각 좌표 방문처리용
        in_mst = [False] * n

        mst_cost = 0        # 결과 반환용
        edges_used = 0      # 몇개의 좌표를 들렸는지 체크용

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)     # 거리, 연결된 좌표 번호

            # 이미 확인된 좌표(최소거리 계산 완료된 좌표)
            if in_mst[curr_node]:
                continue

            in_mst[curr_node] = True            # 처리된 노드
            mst_cost += weight                  # 최소값 누적
            edges_used += 1                     # 확인된 노드 개수

            for next_node in range(n):
                if not in_mst[next_node]:       # 처리 되지 않은 좌표와의 거리 최소값 저장
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + \
                                  abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (next_weight, next_node))

        return mst_cost