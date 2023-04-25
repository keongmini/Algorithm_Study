def solution(s):
    strings = s.split(" ")

    result = ''

    for char in strings:
        for j in range(len(char)):
            if j % 2 == 1:
                result += char[j].lower()
            else:
                result += char[j].upper()
        result += ' '

    return result[:-1]

# 주의사항! split(" ") - 공백이 여러개일 경우 처리할 수 있음 / split() X