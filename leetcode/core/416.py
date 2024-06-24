class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)

        if total % 2 == 1:          # 전체 합이 홀수일 경우, 답이 나올 수 없음
            return False

        target = total // 2         # 모든 수를 다 사용해야 하기 때문에 합이 정확히 전체를 2로 나눈 값이 나와야 함

        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]            # 현재 값, 현재 값 - num 두개의 값만 비교 => 현재 값 - num 에서 + num을 했을 때 내가 나온다 => 현재 값을 구할 수 있다.

        return dp[target]


        # [1, 1, 2, 2] -> True 실패
        # nums.sort()
        #
        # x, y = 0, len(nums) - 1
        # left, right = 0, nums[-1]
        #
        # while x < y:
        #     if left + nums[x] < right:
        #         left += nums[x]
        #         x += 1
        #     elif left + nums[x] > right:
        #         y -= 1
        #         right += nums[y]
        #     else:
        #         if x == y - 1:
        #             return True
        #         else:
        #             left += nums[x]
        #             x += 1
        #
        # return False

s = Solution()
print(s.canPartition([1,3,4,4]))

# 시간 복잡도 O(N * target)
# 공간 복잡도 O(target) 대략 O(1)