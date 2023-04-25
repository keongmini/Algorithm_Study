def solution(n):
    result = '수박' * (n // 2)

    if n % 2 == 1:
        result += '수'

    return result