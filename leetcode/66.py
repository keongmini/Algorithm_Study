class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num += str(i)

        num = int(num) + 1

        return list(str(num))