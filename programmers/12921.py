def solution(n):
    def check(x):

        for i in range(2, int(x ** (1 / 2)) + 1):
            if x % i == 0:
                return False

        return True

    result = 0
    for i in range(2, n + 1):
        if check(i):
            result += 1

    return result