class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 200
        for str in strs:
            length = min(length, len(str))

        prefix = ''
        for i in range(length):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if current != strs[j][i]:
                    return prefix
            prefix += current

        return prefix
