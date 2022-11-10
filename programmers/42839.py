from itertools import permutations
def solution(numbers):
    nums = set()
    for l in range(1, len(numbers) + 1):
        for p in permutations(numbers, l):
            tmp = ''.join(p)
            nums.add(int(tmp))

    def prime(n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = 0
    for num in nums:
        if prime(num):
            result += 1

    return result