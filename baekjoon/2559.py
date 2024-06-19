T, K = map(int, input().split())

temperatures = list(map(int, input().split()))

result = sum(temperatures[:K])
now = result

for i in range(T - K):
    now -= temperatures[i]
    now += temperatures[i + K]

    result = max(result, now)

print(result)

# result = max(result, sum(temperatures[i:i+K]))      # sum 시간복잡도 O(n) -> 시간초과 발생