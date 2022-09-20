def solution(rows, columns, queries):
    cnt = 0
    result = []

    graph = []
    start = 1
    for _ in range(rows):
        row = [i for i in range(start, columns + start)]
        graph.append(row)
        start += columns                # 주의할 부분: 행과 열이 다른 크기를 갖음 -> 열의 길이 만큼 더해주어야 원하는 그래프 생성 가능

    while cnt < len(queries):
        x1, y1, x2, y2 = [num - 1 for num in queries[cnt]]
        minNum = rows * columns

        nowx, nowy = x1, y1
        tmp = graph[nowx][nowy]
        check = 1
        while (nowx != x1 and nowy != y1) or check == 1:

            if nowx == x1 and nowy < y2:
                nowy += 1
            elif nowx < x2 and nowy == y2:
                nowx += 1
            elif nowx == x2 and nowy > y1:
                nowy -= 1
            elif nowx > x1 and nowy == y1:
                nowx -= 1
            else:
                continue

            tmp, graph[nowx][nowy] = graph[nowx][nowy], tmp
            minNum = min(minNum, tmp)

            if nowx == x1 and nowy == y1:
                check = 0

        result.append(minNum)
        cnt += 1

    return result