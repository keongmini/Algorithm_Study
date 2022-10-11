# 실패
def solution(A):
    A.sort()

    if A[0] >= 0:
        return A[0] + A[1]

    if A[-1] <= 0:
        return abs(A[-1] + A[-2])

    left = 0
    right = len(A) - 1
    result = int(1e9) * 2
    while A[left] < 0:
        while A[right] >= 0:
            if abs(A[left] + A[right]) < result:
                result = abs(A[left] + A[right])
            right -= 1
        left += 1
        right = len(A) - 1

    return result

# 참고 https://velog.io/@dpdnm/Codility-Lesson-15-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-MinAbsSumOfTwo
def solution(A):
    A.sort(key=lambda x : abs(x))

    minNum = abs(A[0] + A[0])

    for i in range(len(A) - 1):
        minNum = min(minNum, abs(A[i] + A[i + 1]))

    return minNum

# 시간복잡도 O(N * log(N))
# https://app.codility.com/demo/results/trainingR67KP3-AB2/