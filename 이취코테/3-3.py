n, m = map(int, input().split())

# 1. 풀이
minNums = []

for _ in range(n):
    nums = list(map(int, input().split()))
    minNums.append(min(nums))

print(max(minNums))

# 2. 풀이
result = 0

for _ in range(n):
    nums = list(map(int, input().split()))
    minNum = min(nums)

    result = max(result, minNum)

print(result)