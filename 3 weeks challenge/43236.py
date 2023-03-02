def solution(distance, rocks, n):
    start = 0
    end = distance

    rocks.sort()

    result = 0
    while start <= end:
        mid = (start + end) // 2  # 거리의 최솟값 중에 큰 값

        now = 0  # 제거된 바위 갯수
        prev = 0  # 현재 바위와의 거리를 구해야하는 바위

        for rock in rocks:
            if rock - prev < mid:
                now += 1
            else:  # mid보다 크면 바위를 제거하지 않음
                prev = rock

        if now > n:     # 제거한 돌의 갯수가 주어진 값보다 많으면 mid를 줄이기
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result
