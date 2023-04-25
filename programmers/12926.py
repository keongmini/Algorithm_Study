def solution(s, n):
    result = ''

    for char in s:
        if char == ' ':
            result += char

        if ord(char) >= 65 and ord(char) <= 90:
            if ord(char) + n > 90:
                now = n - (90 - ord(char)) + 64
                result += chr(now)
            else:
                result += chr(ord(char) + n)

        if ord(char) >= 97 and ord(char) <= 122:
            if ord(char) + n > 122:
                now = n - (122 - ord(char)) + 96
                result += chr(now)
            else:
                result += chr(ord(char) + n)

    return result