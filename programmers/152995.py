# 실패
def solution(scores):
    check = scores[0]

    scores.sort(key=lambda x: sum(x), reverse=True)

    if scores[0][0] > check[0] and scores[0][1] > check[1]:
        return -1

    return scores.index(check) + 1