# 슬라이딩 윈도우 - 더 이상 사용하지 않는 값을 저장하지 않고 배열 갱신

# 참고 https://my-coding-notes.tistory.com/318

N = int(input())

first = list(map(int, input().split()))
maxDP = first
minDP = first
# 첫번째 배열 동일

for _ in range(N - 1):
    n1, n2, n3 = map(int, input().split())
    maxDP = [n1 + max(maxDP[0], maxDP[1]), n2 + max(maxDP), n3 + max(maxDP[1], maxDP[2])]       # 이전 값 중에 큰 거 + 현재 값
    minDP = [n1 + min(minDP[0], minDP[1]), n2 + min(minDP), n3 + min(minDP[1], minDP[2])]       # 이전 값 중에 작은 거 + 현재 값
    # 계속 갱신하기 때문에 한줄씩만 저장됨
    
print(max(maxDP), min(minDP))

# 단순 DP - 메모리 초과
#
# N = int(input())
#
# graph = []
# for _ in range(N):
#     now = list(map(int, input().split()))
#     graph.append(now)
#
# dp = [[0, 0, 0] for _ in range(N)]
# dp[0] = graph[0]
#
# # 최대
# for i in range(N - 1):
#     for j in range(3):
#         if j == 0:
#             dp[i + 1][j] = dp[i][j] + graph[i + 1][j]
#             dp[i + 1][j + 1] = dp[i][j] + graph[i + 1][j + 1]
#
#         elif j == 1:
#             dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j] + graph[i + 1][j - 1])
#             dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + graph[i + 1][j])
#             dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + graph[i + 1][j + 1])
#
#         elif j == 2:
#             dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j] + graph[i + 1][j - 1])
#             dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + graph[i + 1][j])
#
# maxNum = max(dp[N - 1])
#
# dp = [[9, 9, 9] for _ in range(N)]
# dp[0] = graph[0]
#
# # 최소
# for i in range(N - 1):
#     for j in range(3):
#         if j == 0:
#             dp[i + 1][j] = dp[i][j] + graph[i + 1][j]
#             dp[i + 1][j + 1] = dp[i][j] + graph[i + 1][j + 1]
#
#         elif j == 1:
#             dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + graph[i + 1][j - 1])
#             dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + graph[i + 1][j])
#             dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + graph[i + 1][j + 1])
#
#         elif j == 2:
#             dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + graph[i + 1][j - 1])
#             dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + graph[i + 1][j])
#
# minNum = min(dp[N - 1])
#
# print(maxNum,minNum)