n = int(input())

scores = []
for _ in range(n):
    data = input().split()
    scores.append([data[0], int(data[1])])

scores.sort(key=lambda x: x[1])

for student in scores:
    print(student[0], end=" ")


