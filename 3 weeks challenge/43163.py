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