import collections

# 예외처리 후 while문으로 확인하는 방식 -> 2가지 케이스에서 시간초과 발생
def solution(queue1, queue2):
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    sumNum = sum1 + sum2
    mid = sumNum // 2

    if (sumNum) % 2 == 1:
        return -1

    for n in queue1 + queue2:
        if n > mid:
            return -1

    result = 0
    while sum1 != mid or sum2 != mid:

        if sum1 < mid:
            popNum = queue2.popleft()
            queue1.append(popNum)
            result += 1
            sum2 -= popNum
            sum1 += popNum

        if sum2 < mid:
            popNum = queue1.popleft()
            queue2.append(popNum)
            result += 1
            sum1 -= popNum
            sum2 += popNum

    return result

# for문으로 반복 횟수 설정 - 통과
def solution(queue1, queue2):
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    sumNum = sum1 + sum2
    mid = sumNum // 2

    if (sumNum) % 2 == 1:
        return -1

    for i in range(len(queue1) * 3):
        if sum1 == sum2:
            return i

        elif sum1 < mid:
            popNum = queue2.popleft()
            queue1.append(popNum)
            sum2 -= popNum
            sum1 += popNum

        elif sum2 < mid:
            popNum = queue1.popleft()
            queue2.append(popNum)
            sum1 -= popNum
            sum2 += popNum

    return -1


# 주의할점! sum함수를 반복적으로 실행하게 되면 시간복잡도가 좋지 않음 -> 값을 연산하는 것이 낫다
# deque의 popleft가 pop(0)보다 효율이 좋다 