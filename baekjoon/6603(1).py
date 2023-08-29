import sys

input = sys.stdin.readline


def check(depth, cnt):
    if depth == 6:
        print(*result)
        return

    for i in range(cnt, k):
        result.append(S[i])
        check(depth + 1, i + 1)
        result.pop()


while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        break

    result = []

    k = nums[0]
    S = nums[1:]

    check(0, 0)

    print()


