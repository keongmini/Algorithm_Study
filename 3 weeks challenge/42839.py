from itertools import permutations


def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    nums = set()
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            tmp = ''.join(p)
            nums.add(int(tmp))

    result = 0
    for num in nums:
        if prime(num):
            result += 1

    return result

