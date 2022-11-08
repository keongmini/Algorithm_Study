# 백준 1197. [최소 스패닝 트리](https://www.acmicpc.net/problem/1197) (골드4)

* 문제 해설 : 최소 스패닝 트리 구현
  
  > 최소 스패닝 트리: 간선의 가중치가 다를 때, 가중치의 합이 최소가 되는 신장 트리
 
  example 1. 
  ```text
  [입력]
    3 3  
    1 2 1  
    2 3 2  
    1 3 3  
  
  [출력]
    3
    ```
  
  제약조건.
  ```text
    첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.  
    그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
  
    첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
    ```
  
* 문제 풀이
  
  - [크루스칼 알고리즘](https://github.com/keongmini/Today-I-Learned/blob/master/Algorithm/Kruskal%20Algorithm.md)
  
  **시간복잡도 O(N * logN)**
  
  ```python
    import heapq
    n, m = map(int, input().split())
    q = []
    
    for _ in range(m):
        a, b, w = map(int, input().split())
        heapq.heappush(q, (w, a, b))        # 가중치를 기준으로 정렬
    
    parent = [i for i in range(n + 1)]
    
    # 유니온 파인드 구현 - 해당 문제에서 파인드 제외
    def getParent(parent, x):
        if parent[x] == x:
            return x
        parent[x] = getParent(parent, parent[x])
        return parent[x]
    
    def unionParent(parent, a, b):
        a = getParent(parent, a)
        b = getParent(parent, b)
    
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    result = 0
    while q:
        w, a, b = heapq.heappop(q)
    
        if getParent(parent, a) != getParent(parent, b):        #  부모 노드 찾기 / 같을 경우 사이클
            unionParent(parent, a, b)       # Union
            result += w
    
    print(result)
    ```