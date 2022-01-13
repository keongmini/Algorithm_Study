def solution(priorities, location):
    itemList = [[v,i] for i, v in enumerate(priorities)]
    answer = []
    while itemList:
        maxNum = max(itemList)[0]
        if itemList[0][0] < maxNum:
            itemList.append(itemList.pop(0))
        else:
            answer.append(itemList.pop(0))
    for item in answer:
        if item[1] == location:
            tmp = answer.index(item)
            break

    return tmp + 1

print(solution([2, 1, 3, 2],2))