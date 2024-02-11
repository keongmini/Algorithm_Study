# in-place 알고리즘: 메모리 공간을 추가적으로 사용하지 않는 알고리즘

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N, M = len(matrix), len(matrix[0])

        zeroIndex = []            # in-place 알고리즘에 맞지 않나..? 
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    zeroIndex.append((i, j))
        
        for x, y in zeroIndex:
            for i in range(N):
                matrix[i][y] = 0
            for j in range(M):
                matrix[x][j] = 0
        
        return matrix

# --

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N, M = len(matrix), len(matrix[0])

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    for x in range(N):
                        if matrix[x][j] != 0:
                            matrix[x][j] = 1e9
                    for y in range(M):
                        if matrix[i][y] != 0:
                            matrix[i][y] = 1e9

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1e9:
                    matrix[i][j] = 0

        return matrix
