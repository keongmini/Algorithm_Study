class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [10001 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for money in range(coin, amount + 1):
                prev = money - coin
                if prev != 10001:
                    dp[money] = min(dp[prev] + 1, dp[money])

        return dp[amount] if dp[amount] != 10001 else -1