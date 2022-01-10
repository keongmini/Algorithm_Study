m = int(input())

for i in range(m):
    paren = input()
    parenList = []
    check = 0
    for i in paren:
        if i == '(':
            parenList.append(i)
        elif i == ')':
            if not parenList:
                check = 1
                break
            parenList.pop()
    if parenList or check:
        print('NO')
    else:
        print('YES')