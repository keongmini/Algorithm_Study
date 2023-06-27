N, K = map(int, input().split())

data = [[0,0]]
result = [[0]*(K+1) for _ in range(N+1)]    # 2차원 배열

for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = data[i][0]
        v = data[i][1]

        if j < w:       # 현재 무게가 비교값보다 더 클 경우
            result[i][j] = result[i-1][j]       # 이전 가치 그대로 가져옴
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-w]+v)      # 이전 가치와 현재 무게를 뺀 상태에 새로운 가치를 더한 값 비교

print(result[N][K])