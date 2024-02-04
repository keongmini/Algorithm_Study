class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])

        for i in intervals:
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result

# ---
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        x, y = intervals[0]

        result = []
        for i, j in intervals[1:]:
            if y >= i:
                y = max(y, j)
            elif y < i:
                result.append([x, y])
                x = i
                y = j

        result.append([x, y])

        return result
