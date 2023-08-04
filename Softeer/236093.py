import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

now = ''

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        if not now:
            now = 'ascending'
        elif now == 'descending':
            now = 'mixed'
            break

    elif nums[i] < nums[i - 1]:
        if not now:
            now = 'descending'
        elif now == 'ascending':
            now = 'mixed'
            break

print(now)