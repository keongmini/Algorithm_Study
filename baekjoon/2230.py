# 투 포인터 풀이 - 통과
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

nums.sort()

left = 0
right = 1

result = nums[-1] - nums[0]

while left <= right and right < N:
    now = nums[right] - nums[left]

    if now > M:
        left += 1
        result = min(result, now)
    elif now < M:
        right += 1
    else:
        result = M
        break

print(result)



# 시간초과
# N, M = map(int, input().split())
#
# nums = []
#
# for _ in range(N):
#     now = int(input())
#     nums.append(now)
#
# nums.sort()
#
# result = 1e9
#
# for i in range(len(nums)  - 1):
#     for j in range(i + 1, len(nums)):
#         tmp = nums[j] - nums[i]
#
#         if tmp >= M:
#             if tmp < result:
#                 result = tmp
#             else:
#                 break
#
# print(result)
