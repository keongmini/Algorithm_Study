N = int(input())

building = list(map(int, input().split()))
building.append(0)
building.append(0)

result = 0

if building[0] > max(building[1:3]):
    result += building[0] - max(building[1:3])

if building[1] > max(building[:1] + building[2:4]):
    result += building[1] - max(building[:1] + building[2:4])

for i in range(2, len(building) - 2):
    pivot = max(building[i - 2: i] + building[i + 1: i + 3])

    if pivot > building[i]:
        continue
    else:
        result += building[i] - pivot

print('#{}'.format(1), result)