from collections import deque

def solution(citations):
    result = len(citations)

    citations.sort(reverse=True)
    citations = deque(citations)

    index = []

    while result > 0:
        while citations and citations[0] >= result:
            index.append(citations.popleft())

        if len(index) >= result:
            break

        result -= 1

    return result

s = solution([3, 3, 5, 8, 25])
print(s)