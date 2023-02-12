N = int(input())

graph = []
teacher = 0
for i in range(N):
    new = input().split()
    graph.append(new)       # 그래프 생성

    teacher += new.count('T')       # 선생님 갯수 세기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def view(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while nx >= 0 and nx < N and ny >= 0 and ny < N and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return False
            else:       # 한칸 더 이동
                nx += dx[i]
                ny += dy[i]
    return True     # 장애물, 학생과 만나지 않음

def backTracking(cnt):      # cnt = 장애물 개수
    global result

    if cnt == 3:            # 장애물 세개 다 설치 완료
        checkTeacher = 0        # 감시를 피한 선생님 갯수 확인용
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'T':
                    if view(i, j) == True:
                        checkTeacher += 1       # 감시를 피한 선생님 갯수 + 1

        if checkTeacher == teacher:
            result = True
        return

    for i in range(N):          # 장애물 설치
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                backTracking(cnt + 1)
                graph[i][j] = 'X'

result = False
backTracking(0)
if result:
    print('YES')
else:
    print('NO')