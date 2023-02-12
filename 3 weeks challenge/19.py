N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxNum = -1e9
minNum = 1e9

def dfs(cnt, num):
    global add, sub, mul, div, maxNum, minNum

    if cnt == N:
        maxNum = max(maxNum, num)
        minNum = min(minNum, num)
    else:
        if add > 0:
            add -= 1
            dfs(cnt + 1, num + A[cnt])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(cnt + 1, num - A[cnt])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(cnt + 1, num * A[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt + 1, int(num / A[cnt]))
            div += 1

dfs(1, A[0])

print(maxNum)
print(minNum)