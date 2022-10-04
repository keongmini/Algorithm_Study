# Timeout Error
# 시간 복잡도 O(N*M)
def solution(N, A):
    result = [0 for _ in range(N)]

    maxNum = 0
    for order in A:
        if order > N:
            result = [maxNum] * N
        else:
            result[order - 1] += 1
            if maxNum < result[order - 1]:
                maxNum = result[order - 1]

    return result


# 시간 복잡도 O(N + M)
def solution(N, A):
    result = [0] * N

    save = 0
    maxNum = 0
    for order in A:
        if order > N:
            save = maxNum                       # 최댓값 갱신
        else:
            if result[order - 1] < save:
                result[order - 1] = save        # 현재의 최댓값보다 작으면 최댓값 + 1 로 처리
            result[order - 1] += 1
            maxNum = max(maxNum, result[order - 1])

    for i in range(len(result)):                # 최댓값 보다 작은 모든 값을 최댓값으로 변경
        if result[i] < save:
            result[i] = save

    return result

# https://app.codility.com/demo/results/training2NEX52-SWR/