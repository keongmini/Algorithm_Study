# 참고 https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/1689443/for-beginners-count-number-of-connected-graphs-o-n-94-faster/?orderBy=most_votes&languageTags=python

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def remove_point(a, b):
            points.discard((a, b))
            for y in x_dic[a]:
                if (a, y) in points:
                    remove_point(a, y)

            for x in y_dic[b]:
                if (x, b) in points:
                    remove_point(x, b)

        x_dic = defaultdict(list)
        y_dic = defaultdict(list)
        points = {(i, j) for i, j in stones}

        for i, j in stones:
            x_dic[i].append(j)
            y_dic[j].append(i)

        cnt = 0
        for a, b in stones:
            if (a, b) in points:
                remove_point(a, b)
                cnt += 1

        return len(stones) - cnt