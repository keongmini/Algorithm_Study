from itertools import permutations

def solution(k, dungeons):
    result = 0

    for permutation in permutations(dungeons, len(dungeons)):
        now = k
        cnt = 0

        for need, use in permutation:
            if now < need:
                continue

            now -= use
            cnt += 1

        result = max(result, cnt)

    return result