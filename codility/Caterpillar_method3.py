# 실패
def solution(A):
    A.sort()

    result = 0
    for i in range(len(A) - 2):
        for j in range(i + 1, len(A) - 1):
            check = 0
            for k in range(j + 1, len(A)):
                if A[i] + A[j] <= A[k]:
                    check = 1
                    break
                else:
                    result += 1

            if check == 1:
                break

    return result

s = solution([10,2,5,1,8,12])

# 통과
# 코딜리티 읽기자료 참고  
def solution(A):
    A.sort()

    result = 0
    for x in range(len(A) - 2):
        z = x + 2
        for y in range(x + 1, len(A) - 1):
            while z < len(A) and A[x] + A[y] > A[z]:
                z += 1

            result += z - y - 1

    return result

# 시간 복잡도 O(N**2)
# https://app.codility.com/demo/results/training46YJ6P-ZSE/