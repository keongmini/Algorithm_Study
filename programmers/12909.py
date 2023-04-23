def solution(s):
    stack = []

    for p in s:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False

            stack.pop()

    if stack:
        return False

    return True