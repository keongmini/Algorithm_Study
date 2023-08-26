# 참고 https://ggasoon2.tistory.com/11
# 재귀적으로 계속 4개 영역으로 쪼개기
# : 4개 영역으로 쪼갠 후 숫자가 포함된 부분을 찾고 또 다시 그 영역을 4개 영역으로 쪼개고.. 의 반복

import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

result = 0

while N != 0:
    N -= 1                              # 현재 크기 기준 반으로 쪼갠다고 생각했을 때 하나 빼줘야 함
    size = 2 ** N

    if r < size and c < size:           # 2사분면
        result += size * size * 0       # 이 자리에 있는 숫자는 무조건 첫번째로 방문하기 때문에

    elif r < size and c >= size:        # 1사분면
        result += size * size * 1
        c -= size                       # 다음 재귀를 위해 영역 쪼개기

    elif r >= size and c < size:        # 3사분면
        result += size * size * 2
        r -= size

    else:                               # 4사분면
        result += size * size * 3
        r -= size
        c -= size

print(result)