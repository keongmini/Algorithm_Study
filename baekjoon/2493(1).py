import sys

input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))

result = [0 for _ in range(len(top))]

stack = []

for i, t in enumerate(top):

    while stack and stack[-1][1] <= t:
        stack.pop()

    if stack:
        result[i] = stack[-1][0] + 1

    stack.append((i, t))

for r in result:
    print(r, end=" ")           # 출력 주의! 리스트 그대로 출력하면 안됨