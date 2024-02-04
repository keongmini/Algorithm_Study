class Solution:
    def spiralOrder(self, matrix):
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 순서가 중요함
        N, M = len(matrix), len(matrix[0])
        visited = [[False for _ in range(M)] for i in range(N)]

        x, y, d = 0, 0, 1  # 현재 좌표, 움직이는 방향(move) 인덱스
        visited[0][0] = True
        result = [matrix[0][0]]

        while True:
            if len(result) == N * M:
                return result

            nx = x + move[d][0]
            ny = y + move[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == True:       # 테두리에 닿으면 방향 변경
                d = (d + 1) % 4
                continue

            result.append(matrix[nx][ny])
            visited[nx][ny] = True
            x, y = nx, ny