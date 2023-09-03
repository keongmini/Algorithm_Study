import sys

input = sys.stdin.readline

N = int(input())

signal = input()

signalList = []

lineSize = N // 5

for i in range(5):
    tmp = signal[lineSize * i: lineSize * (i + 1)]
    signalList.append([t for t in tmp])

nums = {
    0: ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    1: ['#', '#', '#', '#', '#'],
    2: ['#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#'],
    3: ['#', '#', '#', '.', '.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#'],
    4: ['#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#', '.', '.', '#'],
    5: ['#', '#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '#', '#', '#', '#'],
    6: ['#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#'],
    7: ['#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#'],
    8: ['#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#'],
    9: ['#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#']
}

x, y = 0, 0

result = []

while True:
    if y >= lineSize:
        break

    if signalList[x][y] != '#':             # 모든 숫자의 좌측 상단은 무조건 '#' 임 - 아닌 경우 비어있는 열이기 때문에 한칸 이동
        y += 1
        continue

    now = []

    for i in range(5):
        for j in range(3):
            if y + j >= lineSize:           # 최대 크기 넘어가면 1 제외한 다른 숫자 아님
                break
            now.append(signalList[x + i][y + j])

    check = False                           # 1 확인해야 할지
    for num in nums:
        if nums[num] == now:
            result.append(num)
            y += 3                          # 한 숫자는 3개의 열을 사용하기 때문에(1 제외)
            check = True
            break

    if not check:
        now = []
        for i in range(5):
            now.append(signalList[x + i][y])

        if now == nums[1]:
            result.append(1)
            y += 1

answer = ''
for r in result:
    answer += str(r)            # 숫자로 반환하면 안됨!!! 첫 글자가 0일 수 있기 때문에

print(answer)


