N, C = map(int, input().split())
nums = list(map(int, input().split()))

count = dict()

for i, num in enumerate(nums):
    if num in count:
        count[num][0] += 1
    else:
        count[num] = [1, i, num]

result = list(count.values())
result.sort(key = lambda x: (-x[0], x[1]))

for a, b, c in result:
    for _ in range(a):
        print(c, end=" ")