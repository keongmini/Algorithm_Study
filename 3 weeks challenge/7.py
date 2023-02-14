N = input()
nums = [int(i) for i in N]

mid = len(N) // 2

if sum(nums[:mid]) == sum(nums[mid:]):
    print('LUCKY')
else:
    print('READY')