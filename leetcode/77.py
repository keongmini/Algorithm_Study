# k를 고려하지 못한 풀이
class Solution(object):
    def combine(self, n, k):
        nums = [i for i in range(1, n+1)]
        result = []

        for i in range((len(nums)-1)):
            for j in range(i+1, len(nums)):
                result.append([nums[i], nums[j]])

        return result

# dfs 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result
