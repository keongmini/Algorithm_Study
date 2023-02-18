n = int(input())
tri = []
for _ in range(n):
    new = list(map(int, input().split()))
    tri.append(new)

nums = [[0 for _ in range(len(t))] for t in tri]
nums.pop()
nums.append(tri[-1])

def dp(i):
    if i != n - 1:
        dp(i + 1)

    if i == 0:
        return

    for k in range(len(tri[i - 1])):
        nums[i - 1][k] = tri[i - 1][k] + max(nums[i][k], nums[i][k + 1])

dp(0)
print(nums[0][0])