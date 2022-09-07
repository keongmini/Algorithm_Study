def balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        elif p[i] == ")":
            cnt -= 1

        if cnt == 0:
            return i + 1

def correct(p):
    match = []
    for i in range(len(p)):
        if p[i] == '(':
            match.append(p[i])
        elif match and p[i] == ')':
            match.pop()
        else:
            return False

    if not match:
        return True
    else:
        return False

def solution(p):
    if not p:
        return p

    result = ""
    idx = balance(p)
    u = p[:idx]
    v = p[idx:]

    if correct(u):
        result = u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        result += ''.join(u)

    return result

s = solution("()))((()")
print(s)
