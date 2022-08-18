n = int(input())

array = list(map(int, input().split()))

d = [0] * 10

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n-1])

# 이전의 값과 2개 전의 값에 현재 값을 더한 값 사이에서 더 큰 값 선택
# 이전의 값와 2개 전의 값 모두 이미 앞에서 연산이 완료된 상태 -> 가져다 사용하기만 하면 됨