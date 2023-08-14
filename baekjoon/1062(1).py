from itertools import combinations
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()
elif K >= 26:
    print(N)
    exit()

checked = set(['a', 'n', 't', 'i', 'c'])

K -= 5

strings = []
need_check = set()
for _ in range(N):
    now = input()[4:-4]
    strings.append(now)

    for s in now:
        if s not in checked:
            need_check.add(s)

def check():
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

combi = combinations(need_check, K)

if not combi:
    print(N)
    exit()

result = 0

for c in combi:
    for char in c:
        checked.add(char)

    tmp = check()
    result = max(result, tmp)

    for char in c:
        checked.remove(char)

print(result)

