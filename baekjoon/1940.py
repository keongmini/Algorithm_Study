import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
ingredient = list(map(int, input().split()))
ingredient.sort()

result = 0

x, y = 0, len(ingredient) - 1

while x < y:
    if ingredient[x] + ingredient[y] == M:
        result += 1
        x += 1
    elif ingredient[x] + ingredient[y] < M:
        x += 1
    else:
        y -= 1

print(result)

# 시간 초과
# for i in range(len(ingredient)):
#     for j in range(len(ingredient) - 1, i, -1):
#         if ingredient[i] + ingredient[j] < M:
#             break
#
#         if ingredient[i] + ingredient[j] == M:
#             result += 1
#             break
#
# print(result)