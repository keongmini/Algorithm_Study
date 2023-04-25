def solution(n):
    result = [i for i in str(n)]

    result.sort(reverse=True)

    return int(''.join(result))