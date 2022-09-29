# 정확성, 효율성 통과 - 다이나믹 프로그래밍
def solution(triangle):
    answer = [[] for _ in range(len(triangle))]
    answer[0] = triangle[0]

    for i in range(1, len(triangle)):
        now = triangle[i]  # [3,8]
        for j in range(len(now)):
            if j == 0:
                result = triangle[i][j] + answer[i - 1][j]
                answer[i].append(result)
            elif j > 0 and j < len(now) - 1:
                result = []
                result.append(triangle[i][j] + answer[i - 1][j - 1])
                result.append(triangle[i][j] + answer[i - 1][j])
                answer[i].append(max(result))
            elif j == len(now) - 1:
                result = triangle[i][j] + answer[i - 1][j - 1]
                answer[i].append(result)

    return max(answer[-1])
