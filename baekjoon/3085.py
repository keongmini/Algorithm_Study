# 참고 https://kbwplace.tistory.com/130

# 전부 다 확인 - 부르타포스

N = int(input())

candy = []
for _ in range(N):
    now = [s for s in input()]
    candy.append(now)

result = 0


def check():                    # 최대 길이 확인용 함수
    global result

    # 행별로 확인
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j - 1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

        cnt = 1

    # 열별로 확인
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if candy[i][j] == candy[i - 1][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1


move = [(1, 0), (0, 1)]         # 왼쪽, 위는 이전에 돌린 오른쪽, 아래와 동일한 작업 - 생략

for i in range(N):
    for j in range(N):

        for a, b in move:
            nx = i + a
            ny = j + b

            if nx >= N or ny >= N:
                continue

            candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]     # 바꿔서 확인한 다음
            check()
            candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]     # 다시 제자리로 돌려놓기

print(result)