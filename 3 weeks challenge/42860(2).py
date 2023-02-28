def solution(name):
    result = 0

    move = len(name) - 1  # 이동횟수 (전체 길이 - 1(원래 위치))

    for i, a in enumerate(name):

        result += min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)  # 현재위치에서 위아래로 이동한 최소 횟수

        next = i + 1  # 연속된 A의 개수 찾기
        while next < len(name) and name[next] == 'A':
            next += 1

        toLeft = 2 * i + (len(name) - next)  # 연속된 A 모임의 왼쪽으로 이동: 왼쪽 부분 두번 + 오른쪽 부분 한번
        toRight = i + 2 * (len(name) - next)  # 연속된 A 모임의 오른쪽으로 이동: 왼쪽 부분 한번 + 오른쪽 부분 두번

        move = min(move, toLeft, toRight)  # 최소 이동횟수 업데이트

    result += move

    return result