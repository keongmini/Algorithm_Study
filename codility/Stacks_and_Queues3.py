def solution(S):
    if not S:
        return 1

    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if not stack:
                return 0

            stack.pop()

    if stack:
        return 0
    else:
        return 1

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/training2YRFY7-6XX/