# 참고: https://hongcoding.tistory.com/118

# python3 - 시간초과, pypy3 - 통과
import sys

input = sys.stdin.readline

graph = []
location = []                       # 0인(채워야 하는) 위치 저장

for i in range(9):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            location.append((i, j))


def row(i, now):                    # 행 확인
    for j in range(9):
        if now == graph[i][j]:
            return False
    return True


def column(i, now):                 # 열 확인
    for j in range(9):
        if now == graph[j][i]:
            return False
    return True


def rectangular(i, j, now):         # 정사각형 확인
    # 현재 인덱스가 9개의 정사각형 중 어디에 해당하는지 찾아서 정사각형의 좌측 상단 부분으로 위치 설정
    ni = (i // 3) * 3
    nj = (j // 3) * 3

    for a in range(3):
        for b in range(3):
            if now == graph[ni + a][nj + b]:
                return False
    return True


def dfs(cnt):
    if cnt == len(location):        # 위치 모두 확인 완료
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=" ")
            print()

        exit()

    for num in range(1, 10):        # 1-9까지 모두 확인
        nx = location[cnt][0]       # 현재 확인 중인 위치(0)
        ny = location[cnt][1]

        if row(nx, num) and column(ny, num) and rectangular(nx, ny, num):           # num이 현재 위치에 들어갈 수 있는 값임
            graph[nx][ny] = num
            dfs(cnt + 1)
            graph[nx][ny] = 0       # 다음 탐색을 위해 돌려놓기


dfs(0)