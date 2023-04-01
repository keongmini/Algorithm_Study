def solution(food):
    result = []

    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            result.append(str(i))

    now = result + ['0'] + result[::-1]

    return ''.join(now)