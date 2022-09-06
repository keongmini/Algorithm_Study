n = input()
length = len(n) // 2

front = [int(i) for i in n[:length]]
back = [int(i) for i in n[length:]]

if sum(front) == sum(back):
    print('LUCKY')
else:
    print('READY')
