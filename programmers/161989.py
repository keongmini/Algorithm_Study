def solution(n, m, section):
    wall = [1 for _ in range(n + 1)]

    for s in section:
        wall[s] = 0

    result = 0
    for i in range(len(wall)):
        if wall[i] == 0:
            if i + m > n:
                result += 1
                break

            for j in range(i, i + m):
                wall[j] = 1
            result += 1

    return result

