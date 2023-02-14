def solution(sizes):
    maxRow = 0
    maxCol = 0

    for x, y in sizes:
        if x >= y:
            maxRow = max(maxRow, x)
            maxCol = max(maxCol, y)
        else:
            maxRow = max(maxRow, y)
            maxCol = max(maxCol, x)

    return maxRow * maxCol