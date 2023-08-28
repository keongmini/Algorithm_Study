import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

result = 0

while N != 0:
    N -= 1
    now = 2 ** N

    if r < now and c >= now:
        result += now * now * 1
        c -= now

    elif r < now and c < now:
        result += now * now * 0

    elif r >= now and c < now:
        result += now * now * 2
        r -= now

    else:
        result += now * now * 3
        r -= now
        c -= now

print(result)
