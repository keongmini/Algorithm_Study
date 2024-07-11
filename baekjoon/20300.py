N = int(input())
nums = list(map(int, input().split()))

nums.sort()

result = []

if len(nums) % 2 == 1:
    result.append(nums[-1])
    nums = nums[:-1]

for i in range(len(nums)//2):
    result.append(nums[i] + nums[-1 - i])

print(max(result))