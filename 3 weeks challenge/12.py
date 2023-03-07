def column(x, y, array):
    if y == 0:  # 바닥에 있는 경우
        return True
    if [x, y - 1, 0] in array or [x - 1, y, 1] in array or [x, y, 1] in array:  # 보의 한쪽 끝 또는 다른 기둥 위에 있는 경우
        return True

    return False


def row(x, y, array):
    if [x, y - 1, 0] in array or [x + 1, y - 1, 0] in array:  # 한쪽 끝이 기둥 위에 있는 경우
        return True
    if [x - 1, y, 1] in array and [x + 1, y, 1] in array:  # 양쪽이 다른 보와 연결된 경우
        return True

    return False


def solution(n, build_frame):
    result = []

    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if a == 0:  # 기둥
                if column(x, y, result):
                    result.append([x, y, a])
            else:  # 보
                if row(x, y, result):
                    result.append([x, y, a])
        else:  # 삭제
            tmp = result.copy()
            tmp.remove([x, y, a])
            check = True

            for x, y, a in tmp:
                if a == 0:
                    if not column(x, y, tmp):
                        check = False
                        break
                else:
                    if not row(x, y, tmp):
                        check = False
                        break

            if check:  # 삭제 가능
                result = tmp.copy()

    result.sort()
    return result

