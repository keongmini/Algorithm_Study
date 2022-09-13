class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = [0] * len(prices)
        idx = 0
        for i in range(1, len(prices)):
            if prices[idx] <= prices[i]:
                result[idx] = max(prices[i] - prices[idx], result[idx])
            else:
                idx = i

        return max(result)