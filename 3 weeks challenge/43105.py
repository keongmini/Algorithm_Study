def solution(triangle):
    nums = [[0 for _ in range(len(t))] for t in triangle]
    nums.pop()
    nums.append(triangle[-1])

    n = len(triangle)

    def dp(i):
        if i != n - 1:
            dp(i + 1)

        if i == 0:
            return

        for k in range(len(triangle[i - 1])):
            nums[i - 1][k] = triangle[i - 1][k] + max(nums[i][k], nums[i][k + 1])

    dp(0)
    return nums[0][0]
