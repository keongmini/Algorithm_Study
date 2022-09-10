# 내 풀이 - 통과
n = int(input())
homeList = list(map(int, input().split()))
homeList.sort()

length = len(homeList)

if length % 2:
    pivot = homeList[length // 2]
    cnt = 0
    for home in homeList:
        cnt += abs(home - pivot)

    print(pivot)

else:
    result = [0, 0]
    pivot1 = homeList[(length // 2)- 1]
    pivot2 = homeList[length // 2]
    for home in homeList:
        result[0] += abs(home - pivot1)
        result[1] += abs(home - pivot2)

    if min(result) == result[0]:
        print(pivot1)
    else:
        print(pivot2)


# 문제의 핵심은 중간값에 안테나를 설치했을 때 최소값을 갖는다는 것!
# 책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])