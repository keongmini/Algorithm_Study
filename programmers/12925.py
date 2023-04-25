def solution(s):
    if s[0] == '-':
        return int(s[1:]) * -1

    return int(s)
