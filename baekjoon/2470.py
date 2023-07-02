# 투포인터

# 참고 https://velog.io/@kcs05008/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%91%90-%EC%9A%A9%EC%95%A1-%EB%B0%B1%EC%A4%80-2470-python

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

l, r = 0, N - 1

result = abs(nums[l] + nums[r])     # 0에 가까운 값

result1 = l
result2 = r

while l < r:
    now = nums[l] + nums[r]

    if abs(now) < result:
        result = abs(now)
        result1 = l
        result2 = r

    if now < 0:
        l += 1
    else:
        r -= 1

print(nums[result1], nums[result2])