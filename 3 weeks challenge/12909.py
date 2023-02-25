def solution(s):
    stack = []

    check = True
    for p in s:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                check = False
                break
            else:
                stack.pop()

    if stack:
        check = False

    return check