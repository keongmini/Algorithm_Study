# 참고: https://devysi0827.tistory.com/22

def exist(self, board, word):
    global answer

    def dfs(x, y, dfs_word,visited, word) :
        global answer
        move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        if dfs_word == len(word)-1:
            answer = True
            return
        else:
            for i in range(4):
                dx = x + move[i][0]
                dy = y + move[i][1]
                if 0<= dx < m and 0<= dy < n and visited[dx][dy] == 0 and board[dx][dy] == word[dfs_word+1]:
                    visited[dx][dy] = 1
                    dfs(dx,dy,dfs_word+1,visited,word)
                    visited[dx][dy] = 0             # 방문처리 돌려놓기

    m = len(board)
    n = len(board[0])
    visited = [[0] * n for _ in range(m)]
    answer = False
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited[i][j] = 1
                dfs(i,j,0,visited, word)
                visited[i][j] = 0           # 방문 처리 돌려놓기

    return answer


# bfs 풀이 -> 해결 불가
# from collections import deque
#
#
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#         N = len(board)
#         M = len(board[0])
#         visited = [[False for _ in range(M)] for i in range(N)]
#
#         def check(x, y, char):
#             q = deque()
#             q.append((x, y, char, 1))
#
#             while q:
#                 a, b, now, idx = q.popleft()
#
#                 if now == word:
#                     return True
#
#                 for i, j in move:
#                     na = a + i
#                     nb = b + j
#
#                     if na < 0 or na >= N or nb < 0 or nb >= M or visited[na][nb]:
#                         continue
#
#                     n_word = now + board[na][nb]
#
#                     if n_word == word[:idx + 1]:
#                         q.append((na, nb, n_word, idx + 1))
#                         visited[na][nb] = True
#
#         for i in range(N):
#             for j in range(M):
#                 if board[i][j] == word[0]:
#                     visited[i][j] = True
#                     if check(i, j, word[0]):
#                         return True
#
#         return False