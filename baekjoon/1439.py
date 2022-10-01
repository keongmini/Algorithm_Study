n = input()
result = [0, 0]

if n[0] == '0':
    result[0] += 1
else:
    result[1] += 1

for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        result[int(n[i])] += 1

print(min(result))