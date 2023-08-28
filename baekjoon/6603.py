# dfs 풀이 - 참고
# 참고: https://ji-gwang.tistory.com/267
def dfs(depth, idx):
    if depth == 6:
        print(*result)
        return

    for i in range(idx, k):
        result.append(S[i])             # 앞 숫자부터 채운 후
        dfs(depth + 1, i + 1)           # 남은 숫자 다 돌기
        result.pop()                    # 확인 후 pop해서 다음 숫자로 넘어가기 (자리 하나 비우기)


while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1 and nums[0] == 0:
        break

    k = nums[0]
    S = nums[1:]

    result = []

    dfs(0, 0)

    print()


# 조합 사용 - 통과
import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1 and nums[0] == 0:
        break

    k = nums[0]
    S = nums[1:]

    for combi in combinations(S, 6):
        combi = list(combi)
        combi.sort()

        for c in combi:
            print(c, end=" ")

        print()

    print()



