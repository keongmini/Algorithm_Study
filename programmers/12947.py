def solution(x):
    nums = [int(i) for i in str(x)]
    num = sum(nums)

    if x % num == 0:
        return True

    return False