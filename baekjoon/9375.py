from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    result = 1
    clothes = defaultdict(int)

    for _ in range(n):
        name, type = input().split()
        clothes[type] += 1

    for key in clothes:
        result *= clothes[key] + 1          # 해당 종류의 옷을 안입는 경우를 포함하기 위해 + 1

    print(result - 1)                       # 모든 옷을 입지 않은 경우 제거를 위해 - 1
