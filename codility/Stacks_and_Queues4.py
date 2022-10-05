def solution(H):
    stack = []
    cnt = 0
    for i in range(len(H)):
        while True:
            if not stack:
                stack.append(H[i])
                break

            elif stack[-1] == H[i]:
                break

            elif stack[-1] < H[i]:
                stack.append(H[i])
                break

            elif stack[-1] > H[i]:
                stack.pop()
                cnt += 1

    return cnt + len(stack)

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/trainingY2PVTU-6YV/