def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]

    for i in range(1, int(yellow ** 0.5) + 1):
        now = yellow % i
        if now != 0:
            continue

        pair = yellow // i
        row = i + 2
        total = (i * 2) + ((pair + 2) * 2)

        if total == brown:
            return [pair + 2, row]