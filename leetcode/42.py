# 투포인터 풀이 : 오른쪽, 왼쪽 각각 비교하면서 이동

class Solution(object):
    def trap(self, height):
        units = 0

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                units += left_max - height[left]
                left += 1
            else:
                units += right_max - height[right]
                right -= 1

        return units

s = Solution()
tmp = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(tmp)