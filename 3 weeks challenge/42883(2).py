def solution(number, k):
    result = []

    for num in number:
        if k == 0:
            result.append(num)
            continue

        if not result:
            result.append(num)
            continue

        if k > 0:
            while result[-1] < num:
                result.pop()
                k -= 1

                if k == 0 or not result:
                    break

        result.append(num)

    if k > 0:
        result = result[:-k]

    return ''.join(result)