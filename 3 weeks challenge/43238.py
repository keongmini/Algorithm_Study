def solution(n, times):
    left = 1
    right = max(times) * n

    result = 0

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break

        if people >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

