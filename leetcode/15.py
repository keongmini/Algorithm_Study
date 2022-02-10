class Solution(object):
    def threeSum(self, nums):
        answer = []
        nums.sort()

        for i in range(len(nums)-2):
            # nums 내 중복값 확인 - 중복값은 같은 결과를 출력하기 때문에 굳이 확인할 필요x
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    # 다음으로 동일한 값이 있을 경우 같은 결과를 출력하기 때문에 다음으로 넘어가기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # sum = 0 확인 후 다음으로 넘어가기 
                    left += 1
                    right -= 1

        return answer

s = Solution()
tmp = s.threeSum([-1,0,1,2,-1,-4])
print(tmp)