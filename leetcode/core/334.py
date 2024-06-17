# 주의: i, j, k가 연속되는 수가 아니어도 됨
import math

class Solution:
    def increasingTriplet(self, nums) -> bool:
        i = j = math.inf            # 1e9는 제약조건 범위 보다 작음!!! math.inf > 1e9

        for num in nums:
            if num <= i:            # 작은 수가 들어올 때마다 i로 먼저 업데이트 (i가 제일 작은 값으로 보장됨)
                i = num
            elif num <= j:
                j = num
            else:                   # num이 i, j보다 크다는 의미 => i < j < num 성립
                return True

        return False
