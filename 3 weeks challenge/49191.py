from collections import defaultdict


def solution(n, results):
    win = defaultdict(set)  # 자기가 이긴 번호
    lose = defaultdict(set)  # 자기가 진 번호

    for w, l in results:
        win[w].add(l)
        lose[l].add(w)

    for i in range(1, n + 1):
        for winner in lose[i]:
            win[winner].update(win[i])

        for loser in win[i]:
            lose[loser].update(lose[i])

    result = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            result += 1

    return result


