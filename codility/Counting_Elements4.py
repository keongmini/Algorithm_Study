# 풀이 1
def solution(A):
    nums = [n for n in A if n > 0]
    nums = list(set(nums))

    if not nums:
        return 1

    nums.sort()

    if len(nums) == nums[-1]:
        return nums[-1] + 1

    left = 0
    right = len(nums) - 1

    while left + 1 < right:
        # for _ in range(3):
        mid = (left + right) // 2

        if nums[mid] > mid + 1:
            right = mid
        else:
            left = mid

    if nums[left] != left + 1:
        return left + 1

    return right + 1

# 풀이 2
def solution(A):
    nums = [n for n in A if n > 0]
    nums = list(set(nums))

    if not nums:
        return 1

    nums.sort()

    if len(nums) == nums[-1]:
        return nums[-1] + 1

    prev = 0
    for n in nums:
        if n - prev > 1:
            return prev + 1
        prev = n

    return prev + 1