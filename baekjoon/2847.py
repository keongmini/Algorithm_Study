N = int(input())

scores = []

for _ in range(N):
    tmp = int(input())
    scores.append(tmp)

scores.reverse()

result = 0

for i in range(1, len(scores)):
    while scores[i] >= scores[i - 1]:
        result += 1
        scores[i] -= 1

print(result)