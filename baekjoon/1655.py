# 힙큐 사용
# 중간값을 찾아야 하기 때문에 최대힙, 최소힙을 이용하여 균형 유지

# 참고 https://hongcoding.tistory.com/93

import heapq
import sys

input = sys.stdin.readline

N = int(input())

maxHeap = []        # 중심을 기준으로 수직선의 왼쪽 (작은 수 방향)
minHeap = []        # 중심을 기준으로 수직선의 오른쪽 (큰 수 방향)

for i in range(N):
    now = int(input())

    if len(maxHeap) == len(minHeap):
        heapq.heappush(maxHeap, -now)
    else:
        heapq.heappush(minHeap, now)

    if minHeap and minHeap[0] < -maxHeap[0]:        # 두 배열 균형 맞춰서 넣다가 더 작은 값이 오른쪽에 저장 되면 자리 바꿔주기
        left = heapq.heappop(maxHeap)
        right = heapq.heappop(minHeap)

        heapq.heappush(maxHeap, -right)
        heapq.heappush(minHeap, -left)

    print(-maxHeap[0])
