# 답도 틀리고 timeerror 발생
import collections

def solution(A):
    q = collections.deque(A)

    q.popleft()
    q.pop()

    nums = sorted(q)
    minIdx = 0

    X = 0
    Z = len(q) - 1

    sumNum = sum(q)

    result = [0]
    while X < Z:
        minNum = nums[minIdx]
        result.append(sumNum - minNum)

        if q[X] > q[Z]:
            tmp = q.pop()
        else:
            tmp = q.popleft()

        sumNum -= tmp
        nums.remove(tmp)
        # if tmp == minNum:
        #     minIdx += 1

        Z -= 1

    return max(result)


# 참고 https://datacodingschool.tistory.com/64
def solution(A):
    front_sum = [0] * len(A)
    back_sum = [0] * len(A)

    for i in range(1, len(A) - 2):                  # 맨 앞을 제외하고 앞에서부터 누적합
        if front_sum[i - 1] + A[i] > 0:
            front_sum[i] = front_sum[i - 1] + A[i]

    for i in range(len(A) - 2, 1, -1):              # 맨 뒤를 제외하고 뒤에서부터 누적합
        if back_sum[i + 1] + A[i] > 0:
            back_sum[i] = back_sum[i + 1] + A[i]

    max_sum = 0

    for i in range(0, len(A) - 2):
        if front_sum[i] + back_sum[i + 2] > max_sum:        # Y 자리 제외하고 더하기
            max_sum = front_sum[i] + back_sum[i + 2]

    return max_sum

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/training4BM92S-4R4/