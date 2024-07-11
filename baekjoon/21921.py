N, X = map(int, input().split())
nums = list(map(int, input().split()))

result = sum(nums[:X])
cnt = 1
prev = sum(nums[:X])

for i in range(N - X):
    prev = prev - nums[i] + nums[i + X]
    if prev > result:
        result = prev
        cnt = 1
    elif prev == result:
        cnt += 1

if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)