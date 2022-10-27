# 이분탐색
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums)  # low = 나올 수 있는 최소값, 빈구간은 있을 수 없기 때문에 배열 내의 가장 큰 값보다는 무조건 합이 크거나 같게 나옴
        high = sum(nums)  # high = 나올 수 있는 최대값, k가 1일 경우에 전체 합이 답이 됨
        while low < high:
            mid = (low + high) // 2
            total = 0  # 구간별 숫자 합
            count = 1  # 다음 값이 들어오기 전에 mid보다 작을 수 있는 개수 세기 => 구간 세기
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    total = num
                    count += 1
            if count > m:  # 주어진 구간보다 더 많은 구간으로 나눠졌으면 합이 더 커져야함
                low = mid + 1
            else:  # 주어진 구간보다 같거나 작게 쪼개졌으면 합이 더 작아질 수 있음
                high = mid

        return high