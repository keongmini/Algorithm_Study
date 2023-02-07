N = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0
while nums:
    current = nums[-1]

    for _ in range(current):
        if not nums:
            break
        nums.pop()

    result += 1

print(result)