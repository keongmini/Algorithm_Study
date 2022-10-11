# 문제 설명
# rung의 개수는 피노나치 수열의 해당 인덱스값이랑 동일 - A
# A와 동일한 인덱스의 B의 값으로 나눈 나머지 구하는 문제

# 참고 https://sustainable-dev.tistory.com/40
# 참고 https://blog.naver.com/PostView.nhn?blogId=alwlren_00&logNo=221627004494&categoryNo=21&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search
def solution(A, B):
    L = len(A)
    maxNum = 2 ** 30
    fib = [0] * (L + 2)
    fib[1] = 1
    for i in range(2, L + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % maxNum

    sol = []
    for i in range(L):
        tmp1 = fib[A[i] + 1]
        tmp2 = 2 ** B[i]
        sol.append(tmp1 % tmp2)
    return sol


s = solution([4,4,5,5,1], [3,2,4,3,1])
print(s)

# 시간복잡도 O(L)
# https://app.codility.com/demo/results/trainingN876B8-FYM/