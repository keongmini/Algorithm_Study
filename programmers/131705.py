from itertools import combinations


def solution(number):
    result = 0

    for combi in combinations(number, 3):
        if sum(combi) == 0:
            result += 1

    return result