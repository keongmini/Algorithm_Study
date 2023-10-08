# dfs 풀이 통과 x - 해당 케이스 처리 x
from collections import defaultdict, deque

def solution(user_id, banned_id):
    checked = defaultdict(set)

    for ban in banned_id:
        for user in user_id:
            length = min(len(ban), len(user))
            flag = True

            for i in range(length):
                if ban[i] == '*':
                    continue

                if ban[i] != user[i]:
                    flag = False

            if flag and len(ban) == len(user):
                checked[ban].add(user)

    result = []
    q = deque()

    for check in checked[banned_id[0]]:
        q.append([check])

    while q:
        now = q.popleft()

        for i in range(len(now), len(banned_id)):
            for check in checked[banned_id[i]]:
                if check in now:
                    continue

                now.append(check)

                if len(now) == len(banned_id):
                    tmp = sorted(now)

                    if tmp not in result:
                        result.append(tmp)

                    now.pop()

                else:
                    q.append(now.copy())
                    now.pop()

    return len(result)


s = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
print(s)