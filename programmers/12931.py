def solution(n):
    result = 0

    for char in str(n):
        result += int(char)

    return result