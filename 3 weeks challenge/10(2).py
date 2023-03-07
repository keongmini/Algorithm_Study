def rotate(key, d):  # 제자리에서 회전만!
    length = len(key)
    result = [[0] * length for _ in range(length)]

    if d % 4 == 0:  # 회전 x
        for r in range(length):
            for c in range(length):
                result[r][c] = key[r][c]
    elif d % 4 == 1:  # 시계방향으로 90도 회전 1번
        for r in range(length):
            for c in range(length):
                result[c][length - r - 1] = key[r][c]
    elif d % 4 == 2:  # 시계방향으로 90도 회전 2번
        for r in range(length):
            for c in range(length):
                result[length - r - 1][length - c - 1] = key[r][c]
    else:  # 시계방향으로 90도 회전 3번
        for r in range(length):
            for c in range(length):
                result[length - c - 1][r] = key[r][c]

    return result


def check(new_lock, lock_length):  # 모든 값이 1인지 확인 = 자물쇠 홈이 다 채워졌는지
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True


def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)

    new_lock = [[0] * (lock_length * 3) for _ in range(lock_length * 3)]  # 3배 더 큰 배열 생성 - 같은 크기의 배열로 테두리 감싸주기

    # 3배 더 큰 배열 중간에 원래 값 설정
    for i in range(lock_length):
        for j in range(lock_length):
            new_lock[lock_length + i][lock_length + j] = lock[i][j]

    for i in range(1, lock_length * 2):  # 자물쇠와 1개라도 연결되는 구간
        for j in range(1, lock_length * 2):
            for d in range(4):
                rotate_key = rotate(key, d)

                for x in range(key_length):
                    for y in range(key_length):
                        new_lock[i + x][j + y] += rotate_key[x][y]

                if check(new_lock, lock_length):
                    return True

                for x in range(key_length):
                    for y in range(key_length):
                        new_lock[i + x][j + y] -= rotate_key[x][y]  # 원래 상태로 되돌려주기

    return False