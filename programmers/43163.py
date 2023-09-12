# 풀이 1
from collections import deque

def solution(begin, target, words):
    result = 0

    visited = [0 for _ in range(len(words))]

    q = deque([(begin, 0)])
    while q:
        now, cnt = q.popleft()

        if now == target:
            result = cnt
            break

        for i in range(len(words)):
            check = 0

            if not visited[i]:
                for j in range(len(now)):
                    if now[j] != words[i][j]:
                        check += 1

                if check == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = 1
    return result


# 풀이 2
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    def bfs():
        q = deque()
        q.append((begin, 0))

        visited = {}

        result = 1e9

        while q:
            now, path = q.popleft()

            if now == target:
                result = min(result, path)
                continue

            for word in words:
                cnt = 0

                if word not in visited:
                    for i in range(len(now)):
                        if now[i] != word[i]:
                            cnt += 1

                    if cnt == 1:
                        q.append((word, path + 1))
                        visited[word] = True

        if result == 1e9:
            return 0
        return result

    return bfs()