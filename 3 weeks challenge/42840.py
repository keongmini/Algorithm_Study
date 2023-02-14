def solution(answers):
    methods = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    result = [0, 0, 0]
    score = []

    for i, method in enumerate(methods):

        for j in range(len(answers)):
            now = j % len(method)
            if answers[j] == method[now]:
                result[i] += 1

        score.append((result[i], i + 1))

    maxScore = max(result)

    result = []
    for s, i in score:
        if maxScore == s:
            result.append(i)

    result.sort()

    return result

