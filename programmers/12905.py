def solution(board):
    result = 0

    for b in board:     # 탐색하지 않는 부분에 1이 있는 경우 처리       ex. [[0, 1, 0]] => 1
        if 1 in b:
            result = 1
            break

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                if board[i][j] > result:
                    result = board[i][j]

    return result ** 2

# 참고 https://dev-note-97.tistory.com/107 (DP)

