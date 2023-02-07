def solution(n, lost, reserve):
    reserve.sort()

    students = [0 if i in lost else 1 for i in range(n + 1)]

    reserve_next = []
    for r in reserve:
        if students[r] == 0:
            students[r] = 1
        else:
            reserve_next.append(r)

    for r in reserve_next:
        if r > 1 and students[r - 1] == 0:
            students[r - 1] = 1
        elif r < n and students[r + 1] == 0:
            students[r + 1] = 1

    n -= students.count(0)
    return n
