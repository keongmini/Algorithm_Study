# class Solution(object):
#     def twoSum(self, nums, target):
#
#         answer = []
#         for idx, num in enumerate(nums):
#             requireNum = target - num
#
#             if requireNum in nums[:idx] or requireNum in nums[idx+1:]:
#                 answer.append(idx)
#                 tmp = nums[idx+1:].index(requireNum) + (idx + 1)
#                 # tmp : 동일한 숫자가 들어있을 경우 원하는 인덱스값을 얻지 못함 -> 첫번째 값을 제외한 리스트에서 인덱스 뽑기
#                 # 위와 같이 nums[idx+1:]로 할 경우 인덱스가 기존의 인덱스보다 (idx+1)만큼 줄기 때문에 +(idx+1) 코드 추가
#                 answer.append(tmp)
#                 break
#
#         return answer
#
# s = Solution()
# print(s.twoSum([3,3],6))

class Solution:
    def wordSquares(self, words):
        length = len(words[0])
        answer = []

        def check(start, result):
            if start >= length:
                answer.append(result)
                return

            item = result[start]

            for char in words:
                if char.startswith(item):
                    prev = result.copy()
                    for r in range(len(result)):
                        result[r] += char[r]
                    check(start + 1, result)
                    result = prev

        for word in words:
            result = [w for w in word]
            check(1, result)

        return answer

s = Solution()
tmp = s.wordSquares(["abat","baba","atan","atal"])
print(tmp)


