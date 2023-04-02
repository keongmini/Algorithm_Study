def solution(babbling):
    result = 0

    can = ["aya", "ye", "woo", "ma"]

    for ba in babbling:
        now = ''
        true = 0
        prev = ''

        for b in ba:
            now += b

            if now in can and now != prev:
                true += 1
                prev = now
                now = ''

        if true and now == '':
            result += 1

    return result
