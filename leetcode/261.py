class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # 노드개수-1과 간선의 개수가 동일하지 않으면 그래프가 끊어져있음 -> not valid tree
        if len(edges) != n - 1: return False

        # 연결된 정보 저장
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        parent = {0: -1}        # 부모 노드 저장
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:       # 이미 확인된 간선
                    continue
                if neighbour in parent:             # 순환 구조 확인
                    return False
                parent[neighbour] = node            # 부모 노드 저장
                queue.append(neighbour)

        return len(parent) == n
