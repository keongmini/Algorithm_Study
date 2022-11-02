# leetcode 642. [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) (hard)

* 문제 해설 : 검색 시스템 만들기
    1. 검색할 수 있는 문장리스트와 각 문장의 hot degree가 주어짐
    1. 검색한 내용에 맞는 값을 top 3개만 출력, hot degree가 큰 순서대로, hot degree가 같으면 다음 글자의 ASCII 숫자가 더 큰 순서대로
    1. 만약 결과가 3개 미만이라면 출력할 수 있는만큼만 출력, 없으면 빈 배열
    1. '#'이 나오기 전까지 입력값을 이전 값과 계속 연결하여 연결 결과를 검색
    1. '#'이 나오면 빈배열 출력, 지금까지 검색한 결과를 시스템에 저장해두기

  example 1. 
  ```text
    Input
    ["AutocompleteSystem", "input", "input", "input", "input"]
    [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
    Output
    [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
    
    Explanation
    AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
    obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
    obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
    obj.input("a"); // return []. There are no sentences that have prefix "i a".
    obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
    ```
  
  제약조건.
  ```text
    n == sentences.length
    n == times.length
    1 <= n <= 100
    1 <= sentences[i].length <= 100
    1 <= times[i] <= 50
    c is a lowercase English letter, a hash '#', or space ' '.
    Each tested sentence will be a sequence of characters c that end with the character '#'.
    Each tested sentence will have a length in the range [1, 200].
    The words in each input sentence are separated by single spaces.
    At most 5000 calls will be made to input.
    ```
  
* Solution 풀이  
  - Trie   
    참고. [disscussion python solution comment](https://leetcode.com/problems/design-search-autocomplete-system/discuss/105386/Python-Clean-Solution-Using-Trie)
  
      1. 주어진 문장들로 Trie 생성
      1. 현재 prefix 기준으로 Trie에서 일치하는 문장 찾기
      1. hot degree 기준으로 정렬 - 같을 경우 문장의 글자 크기 순서대로 연결(ASCII코드 순서 = 알파벳 정렬 순서)
      1. '#' 입력시 현재까지 prefix를 Trie에 추가
        
      **시간복잡도 Trie 생성: O(N * M), Input: O(N)**
      
      ```python
        class Trie:
            def __init__(self):
                self.node = {}
                self.words = []
        
        class AutocompleteSystem:
            def __init__(self, sentences, times):
                self.trie = Trie()
                self.cache_count = {}
                self.keyword = ""
                for i, sen in enumerate(sentences):
                    self._add_word(sen, self.trie)
                    self.cache_count[sen] = times[i]
        
            def _add_word(self, word, trie):            # Trie 생성
                for char in word:
                    if char not in trie.node:
                        trie.node[char] = Trie()
                    trie = trie.node[char]
                    trie.words.append(word)
                return True
        
            def _find_words(self, word):
                trie = self.trie
                for char in word:
                    if char in trie.node:
                        trie = trie.node[char]
                    else:
                        return []
                return trie.words
        
            def input(self, c):
                if c != '#':
                    self.keyword = self.keyword + c
                    words = self._find_words(self.keyword)
                    res = []
                    for word in words:
                        res.append((self.cache_count[word], word))
                    res = list(set(res))
                    return [s[1] for s in sorted(res, key=lambda x: (-x[0], x[1]))[:3]]
                else:
                    self.cache_count[self.keyword] = self.cache_count.get(self.keyword,0) +1
                    self._add_word(self.keyword,self.trie)
                    self.keyword = ""
                    
                return []
        ```