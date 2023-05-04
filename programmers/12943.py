def solution(num):
    result = 0

    while num != 1:
        if num % 2 == 0:
            num = num // 2
            result += 1

        elif num % 2 == 1:
            num = (num * 3) + 1
            result += 1

        if result >= 500:
            return -1

    return result