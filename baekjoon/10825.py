N = int(input())

students = []
for _ in range(N):
    stu = input().split()
    students.append(stu)

students.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for student in students:
    print(student[0])
