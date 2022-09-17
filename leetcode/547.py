class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def check(idx):
            visited[idx] = True
            for i in range(len(isConnected[idx])):
                if isConnected[idx][i] == 1:
                    isConnected[idx][i] = -1
                    isConnected[i][idx] = -1
                    check(i)

        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            isConnected[i][i] = -1

        cnt = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                check(i)
                cnt += 1

        return cnt

