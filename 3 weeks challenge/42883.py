def solution(number, k):
    result = []

    for num in number:
        if not result:
            result.append(num)
            continue

        if k > 0:
            while result[-1] < num:
                result.pop()
                k -= 1
                if len(result) == 0 or k <= 0:
                    break

        result.append(num)

    if k > 0:
        result = result[:-k]

    return ''.join(result)

s = solution("33333", 3)