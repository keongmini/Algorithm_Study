from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    fx, fy = pos[0]
    bx, by = pos[1]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in dirs:
        nfx, nfy = fx + dx, fy + dy
        nbx, nby = bx + dx, by + dy
        if board[nfx][nfy] == board[nbx][nby] == 0:
            next_pos.append({(nfx, nfy), (nbx, nby)})

    if fx == bx:
        for i in [1, -1]:
            if board[fx + i][fy] == board[bx + i][by] == 0:
                next_pos.append({(fx, fy), (fx + i, fy)})
                next_pos.append({(bx, by), (bx + i, by)})
    elif fy == by:
        for i in [1, -1]:
            if board[fx][fy + i] == board[bx][by + i] == 0:
                next_pos.append({(fx, fy), (fx, fy + i)})
                next_pos.append({(bx, by), (bx, by + i)})

    return next_pos


def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque([({(1, 1), (1, 2)}, 0)])
    visited = []

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, cost + 1))
    return answer