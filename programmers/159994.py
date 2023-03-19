def solution(cards1, cards2, goal):
    result = 0

    for g in goal:
        if cards1 and g == cards1[0]:
            cards1.pop(0)
            result += 1
        elif cards2 and g == cards2[0]:
            cards2.pop(0)
            result += 1
        else:
            return "No"

    if result == len(goal):
        return "Yes"

    return "No"
