n = int(input())
m = list(map(int, input().split()))

maxNum = max(m)
sumNum = 0

for i in m:
    sumNum += i / maxNum * 100

print(sumNum / len(m))