# Timeout Error
# 시간복잡도 O(N**2)
def solution(A):
    dis = [(i - A[i], i + A[i]) for i in range(len(A))]

    cnt = 0
    for i in range(len(dis) - 1):
        now = dis[i]
        for j in range(i + 1, len(dis)):
            if dis[j][0] <= now[1]:
                cnt += 1

    return cnt

# x좌표 위에 모든 원의 시작점과 끝점을 표시했다고 가정 했을 때
# 가장 작은 값부터 차례대로 확인할 때
# 시작점이 계속 이어지게 되면 원이 계속 겹치고 있다는 의미
# 끝점이 나오면 이어지던 원들 중 어떤 원은 끝남
# 이후에 나오는 원은 이전에 끊어진 원과 겹치지 않음
# 참고 https://jayb-log.tistory.com/142?category=867478

def solution(A):
    dis = []
    for i in range(len(A)):
        dis.append((i - A[i], -1))      # 시작점 저장
        dis.append((i + A[i], 1))       # 끝점 저장

    dis.sort()                          # 좌표 위의 점 차례대로 정렬
    cnt = 0                             # 결과값 개수
    intersetion = 0                     # 현재 겹치는 개수

    for d in dis:
        if d[1] == 1:
            intersetion -= 1
        else:
            cnt += intersetion
            intersetion += 1

    return cnt if cnt <= 10000000 else -1

# 시간 복잡도 O(N*log(N)) or O(N)

# https://app.codility.com/demo/results/trainingZ2FMXQ-YQ4/