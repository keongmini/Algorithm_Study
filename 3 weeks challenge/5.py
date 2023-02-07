N, M = map(int, input().split())
nums = [0 for i in range(M + 1)]

weight = list(map(int, input().split()))
for w in weight:
    nums[w] += 1

result = 0
for w in weight:

    result += N - nums[w]
    nums[w] -= 1
    N -= 1

print(result)