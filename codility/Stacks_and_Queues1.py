def solution(S):
    if not S:
        return 1

    if S.isalpha():
        return 1

    pair = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    stack = []

    for s in S:
        if s not in pair:
            stack.append(s)
        else:
            if not stack or pair[s] != stack.pop():
                return 0

    if stack:
        return 0

    return 1

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingJ8MKYY-5PM/