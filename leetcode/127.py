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