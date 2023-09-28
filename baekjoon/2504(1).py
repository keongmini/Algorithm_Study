# 참고 https://www.jongung.com/283

import sys

input = sys.stdin.readline

paren = input()

stack = []

result = 0
tmp = 1             # 임시 저장용

# 분배법칙으로 계산하듯이 처리하는 방식
for i, p in enumerate(paren):
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

        if paren[i - 1] == '(':
            result += tmp

        stack.pop()
        tmp //= 2

    elif p == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break

        if paren[i - 1] == '[':
            result += tmp

        stack.pop()
        tmp //= 3

if stack:               # 남아있으면 올바르지 않은 괄호
    result = 0

print(result)