def solution(s):
    result = 0

    o = 0
    x = 0

    now = s[0]

    for i in range(len(s)):
        char = s[i]

        if char == now:
            o += 1
        else:
            x += 1

        if o == x:
            result += 1
            o = 0
            x = 0
            if i < len(s) - 1:
                now = s[i + 1]

    if o > 0 or x > 0:
        return result + 1

    return result