nums = [int(i) for i in input()]

result = 0
for num in nums:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)