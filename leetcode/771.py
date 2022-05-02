# 파이썬 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        jewels_list = [i for i in jewels]

        for stone in stones:
            if stone in jewels_list:
                cnt += 1

        return cnt

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

# 해시테이블 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        cnt = 0

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in jewels:
            if char in freqs:
                cnt += freqs[char]

        return cnt

# collections.defaultDict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count

# collections.Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            count += freqs[char]

        return count