N = int(input())
nums = list(map(int, input().split()))
nums.sort()

now = 1
for num in nums:
    if now < num:
        break
    now += num

print(now)