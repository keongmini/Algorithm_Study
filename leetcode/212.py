# dfs 풀이 - 실패
import collections
class Solution:
    def findWords(self, board, words):
        letters = collections.defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                letters[board[i][j]].append((i, j))

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        result = []

        def check(x, y, n, idx, visited):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or len(n) < idx or visited[x][y]:
                return False

            if len(n) - 1 == idx and board[x][y] == n[idx]:
                result.append(n)
                return True

            if board[x][y] == n[idx]:
                visited[x][y] = True
                for a, b in d:
                    if check(x + a, y + b, n, idx + 1, visited):
                        return True
                    else:
                        visited[x][y] = False

            return False

        for word in words:
            visited = [[False for _ in range(len(board[0]))] for i in range(len(board))]
            if word[0] in letters:
                for x, y in letters[word[0]]:
                    if check(x, y, word, 0, visited):
                        break

        return result

# Trie 풀이 - solution
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})      # letter가 존재 하지 않으면 추가해줌, node에 현재 딕셔너리의 value값 저장
            node[WORD_KEY] = word       # 마지막 제일 안쪽에 임의의 key값 저장 - 문자열 끝까지 확인했는지 확인하기 위해

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            word_match = currNode.pop(WORD_KEY, False)      # word_key 값을 제거 하거나 word_key가 없으면 False 반환
            if word_match:
                matchedWords.append(word_match)     # word_key는 트라이의 가장 안쪽에 있는 값 - 어떤 값이 있다는 건 확인이 끝났다는 의미

            board[row][col] = '#'       # 방문 처리

            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            board[row][col] = letter        # 다음 확인을 위해 다시 적용

            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords

s = Solution()
print(s.findWords([["a","b","c"],["a","e","d"],["a","f","g"]], ["eaabcdgfa"]))