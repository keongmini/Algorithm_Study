def solution(answers):
    methods = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    result = [0, 0, 0]
    length = [len(method) for method in methods]

    for i, a in enumerate(answers):
        for j, m in enumerate(methods):
            now = i % length[j]

            if m[now] == a:
                result[j] += 1

    maxNum = max(result)
    answer = [r + 1 for r in range(3) if result[r] == maxNum]

    answer.sort()
    return answer