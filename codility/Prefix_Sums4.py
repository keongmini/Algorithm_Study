# 전체 arrary의 평균의 요소가 2개인 array의 평균보다 크거나 작을 수 없음
# 원소가 홀수개로 묶일 경우 3으로 나누는 경우도 생각해줘야 함
# 결론 : 2,3으로 나누는 경우만 고려하면 됨

def solution(A):
    minNum = (A[0] + A[1]) / 2
    result = 0

    for i in range(1, len(A) - 1):
        now = (A[i] + A[i + 1]) / 2
        if minNum > now:
            minNum = now
            result = i

    for i in range(len(A) - 2):
        now = (A[i] + A[i + 1] + A[i + 2]) / 3
        if minNum > now:
            minNum = now
            result = i

    return result

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingFDE82K-XMW/