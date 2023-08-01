# 참고 https://dallae7.tistory.com/158

from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]           # 상하좌우로 움직이면서 값 저장하거나 뺄 용도


def rotate():
    q = deque()
    for d in range(min(N, M) // 2):
        x = d
        y = d

        # 모든 값 1차원 배얄에 저장
        for i, j in move:
            while True:
                nx = x + i
                ny = y + j

                if nx < d or nx >= N - d or ny < d or ny >= M - d:      # 범위에서 벗어나면 break
                    break

                q.append(graph[x][y])       # 돌아가면서 모든 값 1차원 배열에 저장
                x = nx                      # 계속 값 갱신하면 마지막에 원래 위치로 돌아옴
                y = ny

        # 2차원 배열 회전하는 과정 - 1차원 배열 뒷쪽에 있던 값들이 앞으로 이동
        for _ in range(R % ((N - d * 2) * 2 + (M - d * 2) * 2 - 4)):        # 주의!! 그냥 R만큼 돌리면 시간초과 발생 / 어떤 계산으로 나온 식인지.. 모르겠음..
            # 이 부분 질문하기!!
            q.appendleft(q.pop())

        # 다시 2차원 배열 만드는 과정
        for i, j in move:
            while True:
                nx = x + i
                ny = y + j

                if nx < d or nx >= N - d or ny < d or ny >= M - d:
                    break

                graph[x][y] = q.popleft()       # 새로운 값 갱신하기
                x = nx
                y = ny

rotate()

for g in graph:
    for i in g:
        print(i, end=" ")
    print()