N, K = map(int, input().split())

nums = [i for i in range(N + 1)]

flag = False

for num in range(2, N + 1):
    cnt = 1
    while num * cnt <= N:
        if nums[num * cnt] != 0:
            nums[num * cnt] = 0
            K -= 1

        if K == 0:
            print(num * cnt)
            exit()

        cnt += 1
