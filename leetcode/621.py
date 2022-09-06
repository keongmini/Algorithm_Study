# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         counter = collections.Counter(tasks)
#         result = 0
#
#         while True:
#             sub_count = 0
#
#             for task, _ in counter.most_common(n + 1):
#                 sub_count += 1
#                 result += 1
#
#                 counter.subtract(task)
#                 counter += collections.Counter()        # 개수가 0인 것 아예 제거
#
#             if not counter:
#                 break
#
#             result += n - sub_count + 1                 # idle 처리
#
#         return result

class Solution:
    def leastInterval(self, tasks, n) -> int:
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        f_max = max(frequencies)
        n_max = frequencies.count(f_max)    # 개수가 가장 많은 알파벳의 개수 -> step끝에 연결되어야 함

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)

s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))