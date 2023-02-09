N = int(input())
house = list(map(int, input().split()))
house.sort()

pivot = (N - 1) // 2

print(house[pivot])