def solution(a, b, n):
    result = 0

    while n >= a:
        q, r = divmod(n, a)

        result += (q * b)

        n = r + (q * b)

    return result