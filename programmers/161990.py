def solution(wallpaper):
    start = []
    end = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                start.append(i)
                end.append(j)

    start.sort()
    end.sort()

    result = [start[0], end[0], start[-1] + 1, end[-1] + 1]

    return result