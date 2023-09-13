# 100점
# 참고 https://aia1235.tistory.com/30
N = int(input())
M = int(input())
S = input()

cursor, count, result = 0, 0, 0             # 현재 인덱스 위치, 찾은 IOI 갯수, 찾은 P의 개수

while cursor < M - 1:
    if S[cursor:cursor + 3] == 'IOI':       # 3칸씩 이동하며 확인
        count += 1
        cursor += 2                         # IOI의 마지막 글자인 I의 인덱스로 이동해야 하기 때문에
        if count == N:
            result += 1
            count -= 1                      # 현재 찾은 글자의 맨 앞에 해당하는 IOI 하나 제거해준다고 생각
    else:
        cursor += 1
        count = 0

print(result)

# # 50점
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# M = int(input())
# S = input()
#
# P = ''
# for i in range(N):
#     P += 'IO'
# P += 'I'
#
#
# def check(string, idx):
#     if string == P:
#         return True
#
#     if len(string) == len(P):
#         return False
#
#     if string[-1] != S[idx + 1]:
#         return check(string + S[idx + 1], idx + 1)
#     else:
#         return False
#
#
# result = 0
#
# for i in range(len(S) - len(P) + 1):
#     if S[i] == 'I':
#         if check('I', i):
#             result += 1
#
# print(result)