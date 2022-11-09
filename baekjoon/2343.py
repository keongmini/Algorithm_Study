# 참고. https://github.com/keongmini/Algorithm_Study/blob/master/Study/Dynamic%20Programming/Split%20Array%20Largest%20Sum.md
# 동일한 문제 - 이분탐색

n, m = map(int, input().split())
nums = list(map(int, input().split()))

low = max(nums)
high = sum(nums)

while low < high:
    mid = (low + high) // 2

    total = 0
    count = 1

    for num in nums:
        if total + num <= mid:
            total += num
        else:
            total = num
            count += 1

    if count > m:
        low = mid + 1
    else:
        high = mid

print(high)