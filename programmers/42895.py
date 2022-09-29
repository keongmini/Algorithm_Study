# 개선 풀이
import collections

def solution(N, number):
    if N == number:
        return 1

    nums = collections.defaultdict(set)

    for idx in range(1, 9):     # 최솟값 8 이상이면 -1
        nums[idx].add(int(str(N) * idx))        # 숫자 이어붙이기

        for i in range(1, idx):
            for num1 in nums[i]:                # i번 연산 & (idx-i)번 연산 => 연산 횟수 idx번
                for num2 in nums[idx - i]:
                    nums[idx].add(num1 * num2)
                    nums[idx].add(num1 + num2)
                    nums[idx].add(num1 - num2)
                    if num2 != 0:
                        nums[idx].add(num1 // num2)

        if number in nums[idx]:
            return idx

    return -1
