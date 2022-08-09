# parametric search
# 최적화 문제 => 결정문제(답이 yes or no)로 변경하여 해결
# 원하는 조건을 만족하는 가장 알맞는 값을 찾는 문제

# 해당 문제에서는 절단기의 높이를 최대 10억까지라고 설정 -> 순차탐색으로 풀이 불가, 이진탐색 떠올리자!
nums, order = list(map(int, input().split()))
order_list = list(map(int, input().split()))

start = 0
end = max(order_list)

result = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for item in order_list:
        if item > mid:
            total += (item - mid)

    if total >= order:
        result = mid        # 최대값일 수 도 있으므로 기록
        start = mid + 1
    else:
        end = mid - 1
    # elif total < order:       # 정확히 주문한 값만큼을 구하는 것이라면 필요하지만 해당 문제에서는 최대값을 구하라고 했음
    #     end = mid - 1
    # else:
    #     print(mid)
    #     break

print(result)