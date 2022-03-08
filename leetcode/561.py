class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        pairs = [[nums[i],nums[i+1]] for i in range(0, len(nums), 2)]

        answer = 0
        for i in pairs:
            answer += i[0]

        return answer

s = Solution()
print(s.arrayPairSum([6,2,6,5,1,2]))