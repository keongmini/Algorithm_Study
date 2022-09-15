class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        i = len(s) - 1
        while i > 0:
            if s[i] in ['V', 'X'] and s[i - 1] == 'I':
                result += (symbols[s[i]] - symbols['I'])
            elif s[i] in ['L', 'C'] and s[i - 1] == 'X':
                result += (symbols[s[i]] - symbols['X'])
            elif s[i] in ['D', 'M'] and s[i - 1] == 'C':
                result += (symbols[s[i]] - symbols['C'])
            else:
                result += symbols[s[i]]
                i -= 1
                continue

            i -= 2

        if i == 0:
            result += symbols[s[0]]

        return result

