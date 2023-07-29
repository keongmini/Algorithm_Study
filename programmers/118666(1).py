def solution(survey, choices):
    types = {
        "A": 0,
        "N": 0,
        "C": 0,
        "F": 0,
        "M": 0,
        "J": 0,
        "R": 0,
        "T": 0
    }

    for i in range(len(survey)):
        num = choices[i]
        now = survey[i]

        if num > 4:
            types[now[1]] += num - 4
        elif num < 4:
            types[now[0]] += 4 - num

    result = ''

    if types['R'] < types['T']:
        result += 'T'
    else:
        result += 'R'

    if types['C'] < types['F']:
        result += 'F'
    else:
        result += 'C'

    if types['J'] < types['M']:
        result += 'M'
    else:
        result += 'J'

    if types['A'] < types['N']:
        result += 'N'
    else:
        result += 'A'

    return result