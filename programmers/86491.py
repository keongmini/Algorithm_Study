def solution(sizes):
    maxRow = 0
    maxColumn = 0

    for r, c in sizes:
        if r >= c:
            maxRow = max(maxRow, r)
            maxColumn = max(maxColumn, c)
        else:
            maxRow = max(maxRow, c)
            maxColumn = max(maxColumn, r)

    return maxRow * maxColumn
