def solution(s):
    mid = len(s) // 2

    if len(s) % 2 == 1:
        return s[mid]

    return s[mid - 1] + s[mid]