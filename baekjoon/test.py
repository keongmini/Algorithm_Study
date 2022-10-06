# 1
def solution(today, terms, privacies):
    term = {}
    for t in terms:
        a, b = t.split()
        term[a] = int(b)

    today = list(map(int, today.split('.')))

    result = []
    for i in range(len(privacies)):
        date, case = privacies[i].split()
        y, m, d = map(int, date.split('.'))
        y += (m + term[case] - 1) // 12
        m = (m + term[case]) % 12 if (m + term[case]) % 12 != 0 else 12

        if y < today[0] or (y == today[0] and m < today[1]) or (y == today[0] and m == today[1] and d <= today[2]):
            result.append(i + 1)

    return result

# 2
def findIndex(numbers):
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] != 0:
            return i
    return -1

def solution(cap, n, deliveries, pickups):
    result = 0

    idxD = findIndex(deliveries)
    idxP = findIndex(pickups)

    while idxD != -1 and idxP != -1:
        result += (max(idxD, idxP) + 1) * 2

        for _ in range(cap):
            if idxD != -1:
                deliveries[idxD] -= 1
                if not deliveries[idxD]:
                    idxD = findIndex(deliveries)

            if idxP != -1:
                pickups[idxP] -= 1
                if not pickups[idxP]:
                    idxP = findIndex(pickups)

    return result


# 5
import collections

def solution(commands):
    rows = collections.defaultdict(list)
    menu = collections.defaultdict(list)
    save = [[0 for _ in range(50)] for _ in range(50)]

    result = []
    for command in commands:
        orders = command.split()

        if orders[0] == 'UPDATE':
            if orders[1].isdigit():
                x, y = int(orders[1]), int(orders[2])
                save[x][y] = orders[3]
                menu[orders[3]].append((x, y))
                if rows[(x, y)]:
                    que = collections.deque([(x, y)])

                    while que:
                        now = que.popleft()
                        for r in rows[(now[0], now[1])]:
                            if save[r[0]][r[1]] == orders[3]:
                                continue
                            save[r[0]][r[1]] = orders[3]
                            menu[orders[3]].append((r[0], r[1]))
                            que.append((r[0], r[1]))
            else:
                if menu[orders[1]]:
                    for m in menu[orders[1]]:
                        save[m[0]][m[1]] = orders[2]
                    menu[orders[1]] = []

        elif orders[0] == 'MERGE':
            x, y, u, v = map(int, orders[1:])
            rows[(x, y)].append((u, v))
            rows[(u, v)].append((x, y))
            if save[x][y]:
                save[u][v] = save[x][y]
            else:
                save[x][y] = save[u][v]

        elif orders[0] == 'UNMERGE':
            x, y = int(orders[1]), int(orders[2])
            que = collections.deque([(x,y)])
            while que:
                now = que.pop()
                for r in rows[(now[0],now[1])]:
                    rows[(r[0], r[1])].remove((now[0], now[1]))
                    que.append((r[0], r[1]))
                    save[r[0]][r[1]] = 0

                rows[(now[0], now[1])] = []

        elif orders[0] == 'PRINT':
            x, y = int(orders[1]), int(orders[2])
            if not save[x][y]:
                result.append("EMPTY")
            else:
                result.append(save[x][y])

    return result


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))


# 6
def solution(n, m, x, y, r, c, k):
    result = []

    def check(x, y, word, k):
        if k == 0:
            if x == r and y == c:
                result.append(word)
            return

        if x < n:
            check(x + 1, y, word + 'd', k - 1)

        if y > 1:
            check(x, y - 1, word + 'l', k - 1)

        if y < m:
            check(x, y + 1, word + 'r', k - 1)

        if x > 1:
            check(x - 1, y, word + 'u', k - 1)

        return

    check(x, y, '', k)

    if result:
        result.sort()
        return result[0]
    else:
        return "impossible"

solution(3, 4, 2, 3, 3, 1, 5)