import collections
from math import ceil

def solution(fees, records):
    info = collections.defaultdict(list)
    number = []
    for record in records:
        time, num, way = record.split()
        time = time.replace(':', '')
        info[num].append((time, way))
        if num not in number:
            number.append(num)

    number.sort()

    for k in info:
        if len(info[k]) % 2 == 1:
            info[k].append(('2359', 'OUT'))

    for n in number:
        now = info[n]
        time = 0
        for i in range(0, len(now), 2):
            if now[i + 1][0][2:] < now[i][0][2:]:
                time += (60 - int(now[i][0][2:])) + int(now[i + 1][0][2:])
                time += (int(now[i + 1][0][:2]) - int(now[i][0][:2]) - 1) * 60
            else:
                time += int(now[i + 1][0][2:]) - int(now[i][0][2:])
                time += (int(now[i + 1][0][:2]) - int(now[i][0][:2])) * 60
        print(time)

        price = 0
        if time > fees[0]:
            price += fees[1]
            time -= fees[0]
            price += ceil(time / fees[2]) * fees[3]
            number[number.index(n)] = price
        else:
            number[number.index(n)] = fees[1]

    return number

