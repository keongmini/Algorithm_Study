import sys

input = sys.stdin.readline

paran = input()

stack = []

result = 0
tmp = 1

for i, p in enumerate(paran):
    if p == '(':
        stack.append(p)
        tmp *= 2

    elif p == '[':
        stack.append(p)
        tmp *= 3

    elif p == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break

        if paran[i - 1] == '(':
            result += tmp

        stack.pop()
        tmp //= 2

    elif p == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break

        if paran[i - 1] == '[':
            result += tmp

        stack.pop()
        tmp //= 3

if stack:
    result = 0

print(result)