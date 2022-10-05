def solution(A, B):
    stack = []
    cnt = 0
    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            if not stack:
                cnt += 1
                continue

            while True:
                if not stack:
                    cnt += 1
                    break

                if stack[-1] < A[i]:
                    stack.pop()

                else:
                    break

    return cnt + len(stack)

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingDCJS89-233/