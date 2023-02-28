from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)

    result = 0
    while len(people) > 1:

        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            result += 1
        else:
            people.pop()
            result += 1

    if people:
        result += 1

    return result


