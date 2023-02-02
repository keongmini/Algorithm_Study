N = int(input())
nums = list(map(int, input().split()))

start = 0
end = len(nums) - 1

result = -1
while start <= end:
    mid = (start + end) // 2

    if nums[mid] < mid:
        start = mid + 1
    elif nums[mid] > mid:
        end = mid - 1
    else:
        result = mid
        break

print(result)
