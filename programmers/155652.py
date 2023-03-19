def solution(s, skip, index):
    result = []

    for char in s:
        idx = ord(char)

        cnt = 0

        while cnt < index:
            idx += 1

            if idx > 122:
                idx = 96 + (idx - 122)

            if chr(idx) not in skip:
                cnt += 1

        result.append(chr(idx))

    return ''.join(result)

