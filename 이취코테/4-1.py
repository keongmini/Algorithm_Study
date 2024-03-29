N = int(input())
directions = input().split()
i, j = 1, 1

# 풀이 1
for d in directions:
    if d == 'L' and j > 1:
        j -= 1
    elif d == 'R' and j < N:
        j += 1
    elif d == 'U' and i > 1:
        i -= 1
    elif d == 'D' and i < N:
        i+= 1

print(i, j)


# 풀이 2
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for d in directions:
    for k in range(len(move_types)):
        if d == move_types[k]:
            ni = i + dx[k]
            nj = j + dy[k]

            if ni < 1 or nj < 1 or ni > N or nj > N:
                continue

            i, j = ni, nj

print(i, j)

# 풀이 3
n = int(input())
order = input().split()

x = y = 1
nx = [0,0,1,-1]
ny = [-1,1,0,0]
direction = ['U', 'D', 'R', 'L']

for o in order:
    idx = direction.index(o)
    if x + nx[idx] < 1 or y + ny[idx] < 1:
        continue
    x += nx[idx]
    y += ny[idx]

print(y, x)
