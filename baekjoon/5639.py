# 참고 https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/

import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def post_order(start, end):
    if start > end:
        return

    root = pre_order[start]
    idx = start + 1

    while idx <= end:                      # 왼쪽 서브트리의 가장 하당 레벨로 이동
        if pre_order[idx] > root:               # 큰 값은 오른쪽 서브트리
            break
        idx += 1

    post_order(start + 1, idx - 1)      # 현재 위치 기준 왼쪽 서브트리로 이동

    post_order(idx, end)                # 현재 위치 기준 오른쪽 서브트리로 이동

    print(root)


pre_order = []
while True:
    try:                                    # 몇개의 값이 입력될지 주어지지 않음
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order) - 1)


