def solution(sequence):
    plus = [s for s in sequence]
    for i in range(0, len(sequence), 2):
        plus[i] = plus[i] * -1

    minus = [s for s in sequence]
    for i in range(1, len(sequence), 2):
        minus[i] = minus[i] * -1

    prev = plus[0]
    for p in range(1, len(plus)):
        plus[p] = max(plus[p], plus[p] + prev)
        prev = plus[p]

    prev = minus[0]
    for m in range(1, len(minus)):
        minus[m] = max(minus[m], minus[m] + prev)
        prev = minus[m]

    return max(max(plus), max(minus))