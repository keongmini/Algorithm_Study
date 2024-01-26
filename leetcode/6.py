class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:            # 한줄일 경우, 그대로
            return s

        result = [[] for _ in range(numRows)]
        now = 0

        status = True       # 내려가는중인지, 올라가는중인지 확인용

        for char in s:
            result[now].append(char)

            if now == 0:
                status = True
            elif now == numRows - 1:
                status = False

            if status == True:
                now += 1
            else:
                now -= 1

        answer = ''
        for i in range(numRows):
            answer += ''.join(result[i])

        return answer
