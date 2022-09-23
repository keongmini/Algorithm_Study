# 효율성 통과 x
def solution(board, skill):
    for w, x, y, u, v, d in skill:
        for i in range(x, u + 1):
            for j in range(y, v + 1):
                if w == 1:
                    board[i][j] -= d
                if w == 2:
                    board[i][j] += d

    cnt = 0
    for b in board:
        cnt += len(list(filter(lambda x: x > 0, b)))

    return cnt


# 누적합 사용 -> O(N)
# 참고 : https://kimjingo.tistory.com/155
def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0: answer += 1

    return answer
