def solution(survey, choices):
    types = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }

    for i in range(len(survey)):
        if choices[i] > 4:
            types[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            types[survey[i][0]] += (4 - choices[i])

    result = ""

    keys = list(types.keys())

    for i in range(0, len(keys), 2):
        if types[keys[i]] >= types[keys[i + 1]]:
            result += keys[i]
        else:
            result += keys[i + 1]

    return result

