N = int(input())
data = []
for _ in range(N):
    new = list(input().split())
    data.append(new)

data.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for d in data:
    print(d[0])