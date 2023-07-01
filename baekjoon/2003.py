N, M = map(int, input().split())
data = list(map(int, input().split()))

# data.sort()         # 정렬XXX -> 주어진 배열 순서대로 더해야 하는 문제!!

l, r = 0, 0                 # 투포인터 인덱스      # l부터 r까지의 합
now = data[0]               # 현재까지 합

result = 0

while True:
    if now < M:
        r += 1
        if r >= N:
            break
        now += data[r]

    elif now == M:
        result += 1
        now -= data[l]
        l += 1
    else:
        now -= data[l]
        l += 1

print(result)


# 의문..
# ex) 5 2 / 5 4 3 2 1
# 위의 예시로 하면 l이 r을 넘어가는 경우가 발생하는데 = 인덱스가 뒤집힘 그래도 통과가됨..
# L < R 의 경우를 추가해주면 틀림..