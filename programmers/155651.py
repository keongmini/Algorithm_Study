import heapq


def solution(book_time):
    times = []
    for start, end in book_time:
        now = []
        h, m = map(int, start.split(":"))
        now.append(h * 60 + m)
        h, m = map(int, end.split(":"))
        now.append(h * 60 + m)

        heapq.heappush(times, now)

    stack = []
    while times:
        start, end = heapq.heappop(times)

        if not stack or stack[0] + 10 > start:
            heapq.heappush(stack, end)

        elif stack[0] + 10 <= start:
            heapq.heappop(stack)
            heapq.heappush(stack, end)

    return len(stack)







