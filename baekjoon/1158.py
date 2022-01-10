m, n = map(int, input().split())

people = [i for i in range(1,m+1)]
removed = []
now = 0

while len(people):
    now += n - 1
    if now >= len(people):
        now = now % len(people)
    removed.append(people.pop(now))

print("<", ', '.join(str(i) for i in removed), ">", sep = '')