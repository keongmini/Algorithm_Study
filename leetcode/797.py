class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # dfs 풀이
        def dfs(graph, start, end, result, answer):
            if start == end:
                output = result[:]
                ouput.append(start)
                answer.append(result)
                return

            if not graph[start]:
                return

            for num in graph[start]:
                result.append(start)
                dfs(graph, num, end, result, answer)
                result.pop()

        answer = []
        dfs(graph, 0, len(graph) - 1, [], answer)
        return answer

        # bfs 풀이
        def bfs(result, end):
            answer = []
            que = collections.deque([result])

            while que:
                now = que.pop()

                if now[-1] == end:
                    answer.append(now)
                    continue

                if not graph[now[-1]]:
                    continue

                for num in graph[now[-1]]:
                    que.append(now + [num])

            return answer

        output = []

        for num in graph[0]:
            for r in bfs([0, num], len(graph) - 1):
                output.append(r)

        return output