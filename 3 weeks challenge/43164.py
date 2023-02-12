from collections import defaultdict


def solution(tickets):
    paths = defaultdict(list)

    for f, t in tickets:
        paths[f].append(t)

    for path in paths:
        paths[path].sort()

    def dfs(now, n):

        if len(now) == n + 1:
            return now

        for i, path in enumerate(paths[now[-1]]):
            paths[now[-1]].pop(i)
            result = dfs(now + [path], n)
            paths[now[-1]].insert(i, path)
            if result:
                return result

    result = dfs(["ICN"], len(tickets))
    return result

s = solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]])
print(s)