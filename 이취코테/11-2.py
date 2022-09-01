# 내 풀이
nums = [int(i) for i in input()]

result = 0
for num in nums:
    if result == 0 or num == 0:
        result += num
    else:
        result *= num

print(result)

# 책 풀이
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num

print(num)

# 내 풀이에서는 1의 경우를 고려하지 않음
# 숫자가 0, 1 일때는 곱하기보다 더하는 것이 더 합리적!
