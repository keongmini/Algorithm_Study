class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        answer = []

        for cnt in counts:
            heapq.heappush(answer, (-counts[cnt], cnt))

        topk = list()

        for _ in range(k):
            topk.append(heapq.heappop(answer)[1])

        return topk