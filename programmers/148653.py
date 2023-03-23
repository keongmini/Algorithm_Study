def solution(storey):
    result = 0

    nums = [s for s in str(storey)]

    prev = 0
    for i in range(len(nums) - 1, -1, -1):
        now = int(nums[i]) + prev

        if now > 5:
            result += (10 - now)
            prev = 1
        elif now < 5:
            result += now
            prev = 0
        else:
            result += now
            if i > 0:
                if int(nums[i - 1]) >= 5:
                    prev = 1
                else:
                    prev = 0

    result += prev

    return result
