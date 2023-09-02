import sys

input = sys.stdin.readline

T = int(input())

# 순서 상관 x - 이동하는 크기는 동일하기 때문에
# 1씩 갈수록 L 회전
# -1씩 갈수록 R 회전
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(T):
    orders = [s for s in input()]
    direction = 0                                   # 현재 향하는 방향
    min_x, min_y, max_x, max_y = 0, 0, 0, 0         # 사각형 크기
    x, y = 0, 0                                     # 현재 위치한 좌표

    for order in orders:
        if order == 'F':
            x += dx[direction]
            y += dy[direction]

        elif order == 'B':
            x -= dx[direction]
            y -= dy[direction]

        elif order == 'L':
            direction += 1
            if direction > 3:       # 배열 크기 4니까
                direction = 0

        elif order == 'R':
            direction -= 1
            if direction < 0:
                direction = 3

        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(abs(max_x - min_x) * abs(max_y - min_y))

