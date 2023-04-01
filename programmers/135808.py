def solution(k, m, score):
    score.sort(reverse=True)

    result = 0
    now = []
    for s in score:
        now.append(s)

        if len(now) == m:
            result += min(now) * m
            now = []

    return result