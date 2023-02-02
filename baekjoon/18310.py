N = int(input())
loc = list(map(int, input().split()))

loc.sort()

mid = loc[(len(loc) - 1) // 2]

print(mid)