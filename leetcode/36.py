class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = [False] * (len(board) + 1)

        for line in board:
            for num in line:
                if num.isdigit():
                    if check[int(num)]:
                        return False
                    check[int(num)] = True
            check = [False] * (len(board) + 1)

        for i in range(9):
            for j in range(9):
                idx = board[j][i]
                if idx.isdigit():
                    if check[int(idx)]:
                        return False
                    check[int(idx)] = True
            check = [False] * (len(board) + 1)

        a = 0
        b = 0
        while a < 9 and b < 9:
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    idx = board[i][j]
                    if idx.isdigit():
                        if check[int(idx)]:
                            return False
                        check[int(idx)] = True
            check = [False] * (len(board) + 1)

            if b == 6:
                a += 3
                b = 0
            else:
                b += 3

        return True

