import sys

input = sys.stdin.readline

A, B = map(int, input().split())

result = 1e9


def dfs(start, end, cnt):
    global result

    if start == end:
        result = min(result, cnt)
        return

    if start > end:
        return

    dfs(start * 2, end, cnt + 1)
    dfs(int(str(start) + '1'), end, cnt + 1)


dfs(A, B, 0)

if result == 1e9:
    print(-1)
else:
    print(result + 1)