# leetcode 127. [Word Ladder](https://leetcode.com/problems/word-ladder/) (hard)

* 문제 해설 : beginword에서 문자열을 한글자씩 바꿔가면서 endword를 만들 때 걸리는 횟수 구하기 (변형되는 문자들은 word_list에 있어야 함), 만약 변형할 수 없다면 0 출력

  example 1. 
  ```text
  Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
  Output: 5
  Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
  ```
  
  example 2.
  ```text
  Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
  Output: 0
  Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
  ```
  
  제약조건.
  ```text
  1 <= beginWord.length <= 10
  endWord.length == beginWord.length
  1 <= wordList.length <= 5000
  wordList[i].length == beginWord.length
  beginWord, endWord, and wordList[i] consist of lowercase English letters.
  beginWord != endWord
  All the words in wordList are unique.
  ```
  
* 문제 접근 방법  
  첫 시작 문자부터 단어들을 모두 트리로 이어서 dfs로 거리를 구하고자 함   
  -> 모든 문자가 이어진 형태가 아니기 때문에 구현 못함
 
* solution 풀이 
  - dfs  
    1. 문제에서는 한글자씩 변형해가면서 최종 문자에 도달하기 원하기 때문에 문자 리스트에 있는 모든 문자를 한글자씩 가리고 모두 딕셔너리에 저장해둠 (ex. hit -> \*it, h\*t, hi\*)  
    1. 문자열과 레벨(변형된 횟수, 1에서 시작)을 dq에 저장 
    1. 문자열의 글자를 하나씩 가리고 가린 것과 동일한 문자열을 이전에 저장해둔 딕셔너리에서 찾기
    1. 찾은 문자열 방문 처리, dq에 저장(레벨은 하나씩 증가)
    1. 이미 방문한 가린 문자열은 모두 제거 (다시 방문 하지 않도록)
    1. endword와 동일한 문자열 발견하면 종료
    
    **시간복잡도 O(M^2 * N)** M은 문자 길이, N은 문자열 리스트 길이 
    
    ```python
    from collections import defaultdict, deque
    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            if endWord not in wordList or not endWord or not beginWord or not wordList:
                return 0
    
            L = len(beginWord)
    
            # 한 글자만 다른 단어를 찾는 과정을 반복해야하기 때문에 -> 단어들의 각 자리를 *로 바꿔서 모두 저장
            all_combo_dict = defaultdict(list)
            for word in wordList:
                for i in range(L):
                    all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
    
            # Queue for BFS
            queue = deque([(beginWord, 1)])     # 단어와 레벨(변형된 횟수)
            visited = {beginWord: True}     # 방문 처리
            while queue:
                current_word, level = queue.popleft()
                for i in range(L):
                    intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
    
                    for word in all_combo_dict[intermediate_word]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, level + 1))
                    all_combo_dict[intermediate_word] = []      # 이미 방문했기 때문에 다시 방문하지 않도록
    
            return 0
    ```
    
* 엣지 케이스
  - 끝문자가 문자열에 없거나 문자열이 비어있는 경우 