n = int(input())

scoreList = []
for _ in range(n):
    info = input().split()
    scoreList.append([info[0]] + list(map(int, info[1:])))

# sortedList = sorted(scoreList, key = lambda x: (-x[1], x[2], -x[3], x[0]))

scoreList.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for student in scoreList:
    print(student[0])

