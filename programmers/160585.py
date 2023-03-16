from collections import defaultdict


def tiktakto(check):
    # 가로 빙고
    for i in range(3):
        if check[i][0] == check[i][1] == check[i][2] == 1:
            return True

    # 세로 빙고
    for i in range(3):
        if check[0][i] == check[1][i] == check[2][i] == 1:
            return True

    # 대각선 빙고
    if check[0][0] == check[1][1] == check[2][2] == 1:
        return True
    if check[0][2] == check[1][1] == check[2][0] == 1:
        return True

    return False


def solution(board):
    length = len(board)

    first = [[0 for _ in range(3)] for _ in range(3)]
    second = [[0 for _ in range(3)] for _ in range(3)]

    n = 0
    m = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                n += 1
                first[i][j] = 1

            elif board[i][j] == 'X':
                m += 1
                second[i][j] = 1

    # 'O'이 선공이 아닌경우
    if n == 0 and m != 0:
        return 0
    if n < m:
        return 0

    # 번갈아가면서 진행되지 않은 경우
    if n - m > 1:
        return 0

    # 한쪽이 성공했으나 멈추지 않은 경우
    if n >= length:
        if tiktakto(first) and tiktakto(second):
            return 0

        if n == m and tiktakto(first):
            return 0

        if n > m and tiktakto(second):
            return 0

    return 1

