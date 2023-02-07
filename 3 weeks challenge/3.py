nums = [int(i) for i in input()]

result = [0, 0]
if nums[0] == 0:
    result[0] += 1
else:
    result[1] += 1

prev = nums[0]
for i in range(1, len(nums)):
    if nums[i] != prev:
        result[nums[i]] += 1
        prev = nums[i]

print(min(result))