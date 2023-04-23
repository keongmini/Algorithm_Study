def solution(nums):
    now = len(set(nums))

    if len(nums) // 2 < now:
        return len(nums) // 2

    return now
