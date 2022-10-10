# Timeout Error
# 시간 복잡도 O(Z * (max(A) + max(B)))

import collections
def solution(A, B):
    maxNum = max(A + B)

    nums = collections.defaultdict(list)
    nums[1] = 0
    for n in range(2, maxNum + 1):
        if not nums[n]:
            nums[n].append(n)
            for j in range(n + n, maxNum + 1, n):
                nums[j].append(n)

    cnt = 0
    for i in range(len(A)):
        if nums[A[i]] == nums[B[i]]:
            cnt += 1

    return cnt

# 유클리드 호제법
import math

def solution(A, B):
    cnt = 0
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        gcd = math.gcd(a, b)

        gcd_a = 0
        gcd_b = 0

        while gcd_a != 1:
            gcd_a = math.gcd(a, gcd)
            a = a // gcd_a

        while gcd_b != 1:
            gcd_b = math.gcd(b, gcd)
            b = b // gcd_b

        if a == 1 and b == 1:
            cnt += 1

    return cnt

# 시간복잡도 O(Z * log(max(A) + max(B))**2)
# https://app.codility.com/demo/results/trainingYCK4W3-K8B/