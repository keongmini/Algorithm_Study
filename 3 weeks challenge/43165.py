def solution(numbers, target):
    cnt = []

    def dfs(num, result):
        if len(numbers) == num:
            if result == target:
                cnt.append(1)
            return

        dfs(num+1, result+numbers[num])
        dfs(num+1, result-numbers[num])

    dfs(0, 0)
    return len(cnt)