from collections import defaultdict


def solution(clothes):
    now = defaultdict(list)

    result = 1

    for clothe, category in clothes:
        now[category].append(clothe)

    for category in now.keys():
        result *= len(now[category]) + 1

    return result - 1