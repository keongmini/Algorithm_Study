'''
n = 컴퓨터 개수
computers = 컴퓨터 연결정보
ex)
[[1, 1, 0],     0번 컴퓨터가 연결된 컴퓨터 : 1
 [1, 1, 0],     1번 컴퓨터가 연결된 컴퓨터 : 0
 [0, 0, 1]]     2번 컴퓨터가 연결된 컴퓨터 : x

대각선 자리 = 본인 = 무조건 1

* 결론 : 1,2 연결됨(네트워크 1), 3번 따로(네트워크 2) ---- 총 2개
'''

def dfs(i, computers, visited):
    visited[i] = True       # 컴퓨터 방문 여부 표시
    for j in range(len(computers[i])):
        if computers[i][j]==1 and visited[j]==False:     # 방문한 적 없는 컴퓨터인지 체크
            dfs(j, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))