import heapq
def solution(operations):
    minq = []
    maxq = []

    def check(operation):
        order, num = operation.split()
        num = int(num)

        if order == 'I':
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
        elif order == 'D':
            if not minq or not maxq:
                return

            if num == 1:
                now = heapq.heappop(maxq)
                minq.remove(-now)
            elif num == -1:
                now = heapq.heappop(minq)
                maxq.remove(-now)

    for operation in operations:
        check(operation)

    if not minq:
        return [0, 0]

    minq.sort()
    return [minq[-1], minq[0]]