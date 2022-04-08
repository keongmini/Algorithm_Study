# Time Limit Exceeded
class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = []

        for i, v in enumerate(temperatures):
            cnt = 1
            for j in range(i + 1, len(temperatures), 1):
                if temperatures[j] > v:
                    answer.append(cnt)
                    break
                elif j == len(temperatures) - 1:
                    answer.append(0)
                cnt += 1

        answer.append(0)

        return answer

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

# Time complexity: O(N)
# O(N^2) 으로 생각할 수 있지만 결국 while문 내 pop은 한번씩밖에 사용되지 않기때문에 N을 넘지 않음
# Space complexity: O(N)