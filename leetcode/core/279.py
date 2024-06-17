class Solution:
    def numSquares(self, n: int) -> int:
        nums = []               # 제곱근 저장
        dp = [1e9 for _ in range(n + 1)]        # 인덱스에 해당하는 숫자를 구성하기 위한 제곱근 개수

        for i in range(1, n + 1):
            sq = i ** 2

            if sq <= n:                        # 구해야 하는 숫자보다 작은 값까지만
                nums.append(sq)
                dp[sq] = 1

            for num in nums:
                if num < i:                     # 현재 숫자보다 작은 값
                    dp[i] = min(dp[i], dp[i - num] + 1)         # 제곱근 개수 비교해서 더 작은 값

        return dp[n]

# 시간 복잡도 O(n * sqrt(n))
# 공간 복잡도 O(n + sqrt(n))

# 반복되는 코드를 하나로 합침 (반복문 1번)
# for i in range(1, n + 1):
#     sq = i ** 2
#
#     if sq > n:
#         break
#
#     nums.append(sq)
#     dp[sq] = 1
#
# for i in range(1, n + 1):
#     for num in nums:
#         if num < i:
#             dp[i] = min(dp[i], dp[i - num] + 1)
