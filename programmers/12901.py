def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    now = 0

    for i in range(a - 1):
        now += month[i]

    now += b - 1

    result = now % 7

    return day[result]