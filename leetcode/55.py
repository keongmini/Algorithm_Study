# 시간초과
import collections
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        visited = [False for _ in range(len(nums))]
        dq = collections.deque([0])
        visited[0] = True

        while dq:
            now = dq.popleft()

            for i in range(nums[now]):
                n = (now + 1) + i
                if n < len(nums) and not visited[n]:
                    dq.append(n)
                    visited[n] = True

                if visited[len(nums) - 1]:
                    return True

        return False

# dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = 0
        for i in range(len(nums)):
            if i > length:
                return False

            length = max(nums[i] + i, length)

        return True