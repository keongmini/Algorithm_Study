# leetcode 212. [Word Search II](https://leetcode.com/problems/word-search-ii/) (hard)

* 문제 해설 : words에 있는 단어 중에 행렬 내에 인접한 문자를 연결하여 만들 수 있는 단어 모두 찾기 

  example 1. 
  ```text
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
    ```
  
  example 2.
  ```text
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []
    ```
  
  제약조건.
  ```text
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.
    ```
  
* 문제접근방법
  1. 행렬에 있는 모든 문자의 위치를 딕셔너리에 저장(key:문자, value:위치)
  2. words에 있는 문자를 하나씩 확인 - dfs를 이용하여 문자열의 첫 문자 위치부터 인접한 값 확인하며 연결해줌
  3. 인접한 동일한 값에 다시 접근하지 않기 위해 방문처리할 리스트 사용
  
  **Wrong Answer**
  ```text
    [통과하지 못한 테스트케이스]
  
    Input = [["a","a"]], ["aaa"]
    output = ["aaa"]
    expected = []
    ```
  
  현재 인덱스값과 문자열 길이 비교, 현재 위치의 문자와 문자열의 인덱스값 비교
  -> 방문 처리가 제대로 진행x, 같은 문자일 경우 통과되는 문제 발생 
  
  ```python
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
    ``` 

* Solution 풀이 
  - Trie + 백트래킹
    1. words에 있는 단어를 딕셔너리에 저장, 문자열의 첫문자부터 마지막 문자까지 딕셔너리 안에 중첩적으로 저장될 수 있도록, 기장 안쪽에 문자열과 임의의 키값을 저장하여 마지막까지 확인이 끝났음을 확인하는 용으로 설정 (ex. oath => {'o' : {'a : {'t' : {'h' : {'oath' : '$'}}}}})
       -> **트라이** 구성 
    2. 백트래킹 하면서 확인, 방문 처리, 방문 후에 다시 원래 값으로 복원(다음 확인을 위해)
    3. 트라이로 연결된 값 중 이미 확인된 값은 제거 (중복으로 확인하지 않도록 - 최적화)
    
    **시간복잡도 O(M(4⋅3^(L−1)))**
    
    ```python
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
    
                if not currNode:            # 현재 딕셔너리가 처리 완료되어 비게 되면 모두 삭제 - 이미 확인된 문자열이므로 다시 들리지 않도록 -> 최적화
                    parent.pop(letter)
    
            for row in range(rowNum):
                for col in range(colNum):
                    if board[row][col] in trie:
                        backtracking(row, col, trie)
    
            return matchedWords
    ```