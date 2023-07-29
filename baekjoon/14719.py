# 투포인터 - 통과
H, W = map(int, input().split())
nums = list(map(int, input().split()))

result = 0

for i in range(1, W - 1):
    left = max(nums[:i])
    right = max(nums[i+ 1: W])

    now = min(left, right)

    if nums[i] < now:
        result += now - nums[i]

print(result)

# 스택 풀이 - 실패
#
# 반례
# 4 8
# 0 1 0 1 4 1 2 1
#
# H, W = map(int, input().split())
# nums = list(map(int, input().split()))
#
# stack = [nums[0]]
#
# result = 0
#
# for i in range(len(nums)):
#     num = nums[i]
#
#     if len(stack) == 1 and stack[0] <= num:
#         stack.pop()
#         stack.append(num)
#         continue
#
#     if stack[0] <= num or i == len(nums) - 1:
#         now = min(stack[0], num)
#         while stack:
#             if stack[-1] > num:
#                 break
#             result += now - stack.pop()
#
#     stack.append(num)
#
# print(result)
