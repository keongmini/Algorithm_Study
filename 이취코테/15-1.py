N, x = map(int, input().split())
nums = list(map(int, input().split()))

result = []

# 시작점
start = 0
end = len(nums) - 1
mid = -1

while start <= end:
    mid = (start + end) // 2

    if nums[mid] < x:
        start = mid + 1
    elif nums[mid] >= x:
        end = mid - 1

result.append(mid)

# 끝점
start = 0
end = len(nums) - 1

mid = -1

while start <= end:
    mid = (start + end) // 2

    if nums[mid] <= x:
        start = mid + 1
    elif nums[mid] > x:
        end = mid - 1

result.append(mid)

if result[1] - result[0] == 0:
    print(-1)
else:
    print(result[1] - result[0])
