def solution(data, col, row_begin, row_end):
    # 2
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # 3
    tmp = []
    for i in range(row_begin - 1, row_end):
        now = 0
        for j in data[i]:
            now += j % (i + 1)
        tmp.append(now)

    # 4
    result = tmp[0]
    for t in range(1, len(tmp)):
        result = result ^ tmp[t]

    return result
