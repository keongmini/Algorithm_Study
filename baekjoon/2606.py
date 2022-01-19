n = int(input())
m = int(input())
items = [[] for _ in range(n+1)]
for i in range(m):
    nodeList = list(map(int, input().split()))
    for j in nodeList:
        if j == nodeList[0]:
            items[j].append(nodeList[1])
        else:
            items[j].append(nodeList[0])

visited = [False for _ in range(n)]
visited.insert(0,0)

def dfs(v):
    visited[v] = True
    for i in items[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True)-1)