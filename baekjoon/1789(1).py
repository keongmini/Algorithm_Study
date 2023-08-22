S = int(input())

result = 0
sumNum = 0

while sumNum <= S:
    result += 1
    sumNum += result

print(result - 1)