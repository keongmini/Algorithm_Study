from collections import deque


def solution(priorities, location):
    result = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)

    maxNum = max(priorities)
    answer = 0
    while priorities:

        while priorities[0] != maxNum:
            priorities.append(priorities.popleft())
            result.append(result.popleft())

        if priorities[0] == maxNum:
            answer += 1
            if result[0] == location:
                break
            priorities.popleft()
            result.popleft()
            maxNum = max(priorities)

    return answer