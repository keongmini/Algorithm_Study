def solution(n):
    now = n + 1

    check = bin(n).count('1')

    while True:
        if bin(now).count('1') == check:
            return now

        now += 1