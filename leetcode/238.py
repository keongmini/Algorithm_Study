# 1번 : Time Limit Exceeded
# class Solution(object):
#     def productExceptSelf(self, nums):
#         answers = []
#         idx = 0
#
#         numsList = []
#         for i, v in enumerate(nums):
#             numsList.append([i,v])
#
#         for i in range(len(numsList)):
#             answer = 1
#             for num in numsList:
#                 if num[0] == idx:
#                     continue
#                 answer *= num[1]
#             idx += 1
#             answers.append(answer)
#
#         return answers

# 2번 : Time Limit Exceeded (python3에서만 가능)
# import math
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answers = []
#         for i in range(len(nums)):
#             answer = math.prod(nums[:i]) * math.prod(nums[i+1:])
#             answers.append(answer)
#
#         return answers

# 3번 : 	Time Limit Exceeded
# class Solution(object):
#     def productExceptSelf(self, nums):
#         answers = [1 for i in range(len(nums))]
#         idx = 0
#         for num in nums:
#             for i in range(len(answers)):
#                 if idx == i:
#                     continue
#                 answers[i] *= num
#             idx += 1
#         return answers

# 4번: 답
# 이중 반복문 != 반복문 두번 런타임 다름
class Solution(object):
    def productExceptSelf(self, nums):
        out = []

        # 왼쪽 곧
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        # 오른쪽 곱
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
