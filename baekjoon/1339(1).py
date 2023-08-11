N = int(input())

char = {}

for _ in range(N):
    tmp = input()
    length = len(tmp) - 1

    for s in tmp:
        if s in char:
            char[s] += (10 ** length)
        else:
            char[s] = (10 ** length)

        length -= 1

nums = list(char.values())
nums.sort(reverse=True)

result = 0
cnt = 9
for num in nums:
    result += (cnt * num)
    cnt -= 1

print(result)