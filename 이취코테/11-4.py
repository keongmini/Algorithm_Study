n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

# 1부터 target - 1까지 모든 금액을 만들 수 있는 상태 => target 은 만들 수 없는 숫자
# 동전이 딱 주어진 크기 개수만큼만! 있음
# 동전 중 1이 포함되어있지 않으면 무조건 1이 답
# 1이 있으면 주어진 동전을 다 더한 값까지는 모두 만들 수 있으면 모두 다 더한 값 그 다음 숫자가 만들 수 없는 숫자
