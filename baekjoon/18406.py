n = list(map(int, input()))

front = 0
end = len(n) - 1

frontSum = 0
endSum = 0

while front < end:
    frontSum += n[front]
    endSum += n[end]

    front += 1
    end -= 1

if frontSum == endSum:
    print("LUCKY")
else:
    print("READY")