def check(num):
    result = 0

    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            result += 1

            if i ** 2 != num:
                result += 1

    return result


def solution(number, limit, power):
    nums = []

    for i in range(1, number + 1):
        now = check(i)

        if now > limit:
            now = power

        nums.append(now)

    return sum(nums)