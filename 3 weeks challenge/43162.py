def dfs(i, computers, visited):
    visited[i] = True
    for j in range(len(computers[i])):
        if computers[i][j]==1 and visited[j]==False:
            dfs(j, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1

    return answer