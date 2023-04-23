def solution(n):
    result = ''

    while n:
        if n % 3 == 0:
            result += '4'
            n = n // 3 - 1
        else:
            result += str(n % 3)
            n = n // 3

    return result[::-1]


# 참고 https://latte-is-horse.tistory.com/127 (수학적 접근)
