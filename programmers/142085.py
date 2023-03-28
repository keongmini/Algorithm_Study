import heapq


def solution(n, k, enemy):
    now = []

    if k >= len(enemy):
        return len(enemy)

    for i in range(k):
        heapq.heappush(now, enemy[i])

    for i in range(k, len(enemy)):
        heapq.heappush(now, enemy[i])
        n -= heapq.heappop(now)

        if n < 0:
            return i

    return len(enemy)


# 실패한 풀이
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)

    stack = []

    for i in range(len(enemy)):
        now = enemy[i]

        while stack and stack[-1] < now and n >= stack[-1]:
            n -= stack.pop()

        if len(stack) < k:
            stack.append(now)
            continue

        if n < now:
            return i
        else:
            n -= now

    return len(enemy)


s = solution(7, 3, [2, 2, 2, 2, 10])
print(s)
