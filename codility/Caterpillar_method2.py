# import collections
#
# # Timeout Error
# # 시간복잡도 O(N * (N + M))
# def solution(M, A):
#     dq = collections.deque(A)
#
#     cnt = 0
#     for i in range(len(A)):
#         now = []
#         for d in dq:
#             if d not in now:
#                 now.append(d)
#                 cnt += 1
#             else:
#                 break
#
#         dq.popleft()
#
#     return cnt
#
#
# # 시간복잡도 O(N * (N + M))
# def solution(M, A):
#     check = collections.deque()
#     length = 0
#     result = 0
#     for a in A:
#         if a in check:
#             while a in check:
#                 check.popleft()
#                 length -= 1
#
#         if a not in check:
#             check.append(a)
#             length += 1
#             result += length
#
#     return result

# 참고 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alwlren_00&logNo=221636715956
def solution(M, A):
    visited = [False for _ in range(M + 1)]
    front = 0
    slices = 0
    for back in range(len(A)):
        while front < len(A) and not visited[A[front]]:
            visited[A[front]] = True
            slices += front - back + 1
            front += 1
        visited[A[back]] = False

    if slices > 1000000000:
        return 1000000000
    return slices

s = solution(6, [3,4,5,3,5,2])
print(s)

# 시간 복잡도 O(N)
# https://app.codility.com/demo/results/trainingJMQ5QK-5QF/