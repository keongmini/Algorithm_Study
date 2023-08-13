# 참고: https://resilient-923.tistory.com/324

from itertools import combinations
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

if K < 5:           # 앞 뒤 글자도 포함 x - 아무것도 배울 수 없음
    print(0)
    exit()
elif K >= 26:       # 모든 알파벳 배울 수 있음
    print(N)
    exit()

checked = {
    'a': True,
    'n': True,
    't': True,
    'i': True,
    'c': True
}

K -= 5              # a, n, t, i, c 미리 제외

check_list = []     # 위 알파벳 빼고 확인해야 할 알파벳 저장
strings = []
for _ in range(N):
    tmp = input()
    tmp = tmp[4:-4]         # 앞뒤 글자빼고 저장
    strings.append(tmp)

    for t in tmp:
        if t not in check_list and t not in checked:
            check_list.append(t)


def check_string():
    cnt = 0
    for string in strings:
        flag = True
        for s in string:
            if s not in checked:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt


result = 0

combi = list(combinations(check_list, K))

if not combi:       # 현재 수로 조합이 만들어지지 않음 - 모든 글자 확인 가능할 정도의 수가 주어짐
    print(N)
    exit()

for c in combi:
    for char in c:
        checked[char] = True

    now = check_string()
    result = max(result, now)

    for char in c:          # 확인 후 돌려놓기
        if char in check_list:
            del checked[char]

print(result)


# # 시간 초과
# from itertools import combinations
# import sys
#
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
#
# if K < 5:
#     print(0)
#     exit()
# elif K >= 26:
#     print(0)
#     exit()
#
# checked = {
#     'a': True,
#     'n': True,
#     't': True,
#     'i': True,
#     'c': True
# }
#
# K -= 5
#
# check_list = []
# strings = []
# for _ in range(N):
#     tmp = input()
#     tmp = tmp[4:-4]
#     strings.append(tmp)
#
#     for t in tmp:
#         if t not in check_list:
#             check_list.append(t)
#
# combi = combinations(check_list, K)
#
# result = 0
#
# for c in combi:
#     cnt = 0
#     for string in strings:
#         flag = True
#         for s in string:
#             if s not in c and s not in checked:
#                 flag = False
#                 break
#         if flag:
#             cnt += 1
#     result = max(result, cnt)
#
# print(result)


# 틀렸습니다.
# N, K = map(int, input().split())
#
# checked = ['a', 'n', 't', 'i', 'c']
#
# K -= 5
#
# if K <= 0:
#     print(0)
#     exit()
#
# if K >= 21:
#     print(N)
#     exit()
#
# char = {}
# nums = {}
#
# for _ in range(N):
#     string = input()
#     string = string[4: -4]
#     set_string = set(string)
#     nums[string] = 0
#
#     for s in set_string:
#         if s in checked:
#             continue
#
#         if s in char:
#             char[s].append(string)
#         else:
#             char[s] = [string]
#         nums[string] += 1
#
# values = list(char.values())
# values.sort(key=lambda x: len(x), reverse=True)
#
# result = 0
#
# for value in values:
#     K -= 1
#     for v in value:
#         nums[v] -= 1
#
#         if nums[v] == 0:
#             result += 1
#
#     if K == 0:
#         break
#
# print(result)