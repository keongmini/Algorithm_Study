# 참고 https://velog.io/@leejy1373/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%95%EB%A0%AC-%EB%B6%88%EB%9F%89%EC%82%AC%EC%9A%A9%EC%9E%90-Python

from itertools import permutations


def check(users, banned_id):            # user id와 banned id 비교 - 해당 자리에 충족하는 유저인지 확인하는 함수
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):      # 문자의 길이가 동일하지 않는 경우 - 절대 충족될 수 없음
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False

    return True


def solution(user_id, banned_id):
    result = []

    for users in permutations(user_id, len(banned_id)):
        if not check(users, banned_id):
            continue
        else:
            users = set(users)                      # 리스트로 비교할 경우 순서가 다르면 다른 리스트로 인식하기 때문에 중복으로 저장 -> set를 이용하면 중복 저장 방지 가능
            if users not in result:
                result.append(users)

    return len(result)

s = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
print(s)


# dfs 풀이 통과 x - 해당 케이스 처리 x
# from collections import defaultdict, deque
#
# def solution(user_id, banned_id):
#     checked = defaultdict(set)
#
#     for ban in banned_id:
#         for user in user_id:
#             length = min(len(ban), len(user))
#             flag = True
#
#             for i in range(length):
#                 if ban[i] == '*':
#                     continue
#
#                 if ban[i] != user[i]:
#                     flag = False
#
#             if flag and len(ban) == len(user):
#                 checked[ban].add(user)
#
#     result = []
#     q = deque()
#
#     for check in checked[banned_id[0]]:
#         q.append([check])
#
#     while q:
#         now = q.popleft()
#
#         for i in range(len(now), len(banned_id)):
#             for check in checked[banned_id[i]]:
#                 if check in now:
#                     continue
#
#                 now.append(check)
#
#                 if len(now) == len(banned_id):
#                     tmp = sorted(now)
#
#                     if tmp not in result:
#                         result.append(tmp)
#
#                     now.pop()
#
#                 else:
#                     q.append(now.copy())
#                     now.pop()
#
#     return len(result)
#
#
# s = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
# print(s)