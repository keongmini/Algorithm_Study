class Trie:
    def __init__(self):
        self.node = {}      # 트라이 연결
        self.words = []     # 해당 값이 포함된 문장 저장

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.cache = {}     # hot degree
        self.keyword = ''

        for i, sentence in enumerate(sentences):
            self.cache[sentence] = times[i]
            self._add_word(sentence, self.trie)

    def _add_word(self, sentence, trie):        # 트라이 생성
        for char in sentence:
            if char not in trie.node:
                trie.node[char] = Trie()
            trie = trie.node[char]
            trie.words.append(sentence)

        return True

    def _find_word(self, word):
        trie = self.trie
        for char in word:
            if char in trie.node:
                trie = trie.node[char]
            else:
                return []

        return trie.words

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.keyword += c
            sentences = self._find_word(self.keyword)
            now = []
            for sentence in sentences:
                now.append((self.cache[sentence], sentence))

            now = list(set(now))
            return [s[1] for s in sorted(now, key=lambda x: (-x[0], x[1]))[:3]]
        else:
            self.cache[self.keyword] = self.cache.get(self.keyword, 0) + 1
            self._add_word(self.keyword, self.trie)
            self.keyword = ''

        return []