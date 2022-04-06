class Solution(object):
    def isValid(self, s):
        parantheses = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        answer = []

        for i in s:
            if i in parantheses.keys():
                answer.append(i)
            else:
                if not answer or parantheses[answer.pop()] != i:
                    return False

        if answer:
            return False
        else:
            return True


class Solution(object):
    def isValid(self, s):
        parantheses = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        answer = []

        for i in s:
            if i not in parantheses:
                answer.append(i)
            elif not answer or parantheses[i] != answer.pop():
                return False

        return len(answer) == 0