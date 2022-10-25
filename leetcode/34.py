# O(N)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        numset = set(nums)

        if target not in numset:
            return [-1, -1]

        start = nums.index(target)

        result = [start]

        for i in range(start, len(nums)):
            if nums[i] != target:
                result.append(i - 1)
                return result

        result.append(len(nums) - 1)
        return result


# 이분탐색 O(log n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound = self.findBound(nums, target, True)        # 시작점 찾기
        if (lower_bound == -1):
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)       # 끝점 찾기

        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)

            if nums[mid] == target:

                if isFirst:     # 시작점을 찾는 경우
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    end = mid - 1
                else:           # 끝점을 찾는 경우
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1