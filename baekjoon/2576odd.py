n = [int(input()) for i in range(7)]

numberSum = 0
minNumber = 100

for i in n:
    if i % 2 == 1:
        numberSum += i
        if minNumber > i:
            minNumber = i

if numberSum == 0:
    print(-1)
else:
    print(numberSum)
    print(minNumber)

