import heapq


def solution(operations):
    minq = []
    maxq = []

    for operation in operations:
        order, num = operation.split()
        num = int(num)

        if order == 'I':
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)

        elif not minq or not maxq:
            continue

        elif order == 'D' and num == 1:
            now = heapq.heappop(maxq)
            minq.remove(-now)

        elif order == 'D' and num == -1:
            now = heapq.heappop(minq)
            maxq.remove(-now)

    if not minq or not maxq:
        return [0, 0]
    else:
        maxNum = heapq.heappop(maxq)
        minNum = heapq.heappop(minq)

        return [-maxNum, minNum]
