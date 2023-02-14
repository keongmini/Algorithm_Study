S = input()
items = [i for i in S]

nums = []
result = []

for item in items:
    if item.isdigit():
        nums.append(int(item))
    else:
        result.append(item)

result.sort()
result.append(str(sum(nums)))

result = ''.join(result)
print(result)