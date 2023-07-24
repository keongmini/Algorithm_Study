string = input()

stack = []

result = 0

for s in string:
    if s not in ['[', ']', '(', ')']:
        stack = []
        break

    if s == '[' or s == '(':
        stack.append(s)

    else:
        now = 0
        flag = True

        if s == ']':
            while stack:
                if stack[-1].isdigit():
                    now += int(stack[-1])
                    stack.pop()
                elif stack[-1] == '[':
                    stack.pop()

                    if now == 0:
                        stack.append('3')
                    else:
                        stack.append(str(now * 3))
                    break

                else:
                    stack = []
                    flag = False
                    break

        elif s == ')':
            while stack:
                if stack[-1].isdigit():
                    now += int(stack[-1])
                    stack.pop()
                elif stack[-1] == '(':
                    stack.pop()

                    if now == 0:
                        stack.append('2')
                    else:
                        stack.append(str(now * 2))
                    break

                else:
                    stack = []
                    flag = False
                    break

        if not stack:
            break

        if not flag:
            break


if stack:
    for s in stack:
        if not s.isdigit():
            result = 0
            break
        result += int(s)

print(result)