# N, R1, C1, R2, C2 = map(int, input().split())
#
# length = 2 * N + 1
#
# shape = [['.' for _ in range(length)] for i in range(length)]
#
# for i in range(N):
#     mid = length // 2
#     for j in range((length // 2) + 1):
#         shape[j][mid] = chr(96 + N - i)
#         shape[length - 1 - j][length - 1 - mid] = chr(96 + N - i)
#
#         mid -= 1
#
# print(shape)


# 참고 https://boomrabbit.tistory.com/181

N, R1, C1, R2, C2 = map(int, input().split())

for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        i1 = i % (2 * N - 1)            # 하나의 마름모 안에서 세로 길이
        j1 = j % (2 * N - 1)            # 하나의 마름모 안에서 가로 길이
        now = abs(N - 1 - i1) + abs(N - 1 - j1)     # a의 위치를 0이라고 하고 현재 위치와 a의 거리 구하기 (거리 = (a x좌표 - 현재 x 좌표) - (b y좌표 - 현재 y좌표))
        # 거리가 같은 모든 위치는 동일한 알파벳을 가지고 있음

        if now >= N:            # 아스키코드 97 + (N - 1) 까지의 알파벳만 사용 (N의 길이만큼 이지만 0 부터 시작하기 때문에 -1)
            print('.', end="")
        else:
            print(chr(97 + now % 26), end="")       # z를 넘어가면 다시 a로 돌아가야 하기 때문에 %26
    print()