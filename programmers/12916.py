def solution(s):
    p_cnt = 0
    y_cnt = 0

    p_cnt += s.count('p')
    p_cnt += s.count('P')

    y_cnt += s.count('y')
    y_cnt += s.count('Y')

    if p_cnt == y_cnt:
        return True

    return False