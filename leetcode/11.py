class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        result = []
        while left < right:
            now = abs(right - left) * min(height[left], height[right])
            result.append(now)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max(result)

    