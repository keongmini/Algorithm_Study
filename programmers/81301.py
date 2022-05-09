def solution(s):
    chars = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    if s.isdigit():
        return int(s)

    answer = []
    tmp = ''
    for char in s:
        if char.isdigit():
            answer.append(char)
            continue
        tmp += char
        if tmp in chars:
            answer.append(chars[tmp])
            tmp = ''

    return int(''.join(answer))