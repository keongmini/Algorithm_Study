# bfs 풀이 - 통과
# 역만 거치는 bfs 말고 연결관계(하이퍼튜브) 고려해야함

# 참고 https://chldkato.tistory.com/57

from collections import deque
import sys

input = sys.stdin.readline

N, K, M = map(int, input().split())
station = [[] for _ in range(N + M + 1)]        # 역과 하이퍼튜브 정보 모두 저장할 배열 = 배열 크기 N + M
path = [0 for _ in range(N + M + 1)]

for i in range(1, M + 1):
    tmp = list(map(int, input().split()))
    for j in range(K):
        station[tmp[j]].append(N + i)       # 역에 연결되는 하이퍼튜브 번호 저장
        station[N + i].append(tmp[j])       # 하이퍼튜브에 연결되는 역 번호 저장

q = deque([1])
path[1] = 1

flag = False

while q:
    now = q.popleft()

    if now == N:
        flag = True
        print(path[now])
        break

    for n in station[now]:
        if not path[n]:     # 방문한 적 없을 때 / 최단거리로 보고 있기 때문
            if n > N:
                path[n] = path[now]     # 연결되는 하이퍼튜브에 현재까지 거리 정보 저장
            else:
                path[n] = path[now] + 1     # 타고 온 하이퍼튜브 + 1 = 새로운 역 도착했기 때문

            q.append(n)


if not flag:
    print(-1)


# # dfs 풀이 - 시간초과 실패
# from collections import defaultdict
#
# N, K, M = map(int, input().split())
#
# station = defaultdict(list)
#
# for _ in range(M):
#     nums = list(map(int, input().split()))
#     for i in range(K):
#         for j in range(i + 1, K):
#             station[nums[i]].append(nums[j])
#             station[nums[j]].append(nums[i])
#
# result = 1e9
#
#
# def dfs(num, visited, now):
#     global result
#
#     visited[num] = True
#
#     for i in station[num]:
#         if i == N:
#             result = min(result, now + 1)
#             return
#
#         if visited[i]:
#             continue
#
#         dfs(i, visited, now + 1)
#
#
# visited = [False for _ in range(N + 1)]
# visited[0] = True
# visited[1] = True
#
# for n in station[1]:
#     visited[n] = True
#
# for n in station[1]:
#     dfs(n, visited, 2)
#
# print(result)

