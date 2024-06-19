class Solution:
    def diffWaysToCompute(self, expression: str):
        if expression.isdigit():                    # 숫자만 들어온 경우 숫자 반환
            return [int(expression)]

        result = []

        for i in range(len(expression)):
            if expression[i] in "-+*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            result.append(l + r)
                        elif expression[i] == "-":
                            result.append(l - r)
                        elif expression[i] == "*":
                            result.append(l * r)

        return result

s = Solution()
s.diffWaysToCompute("2-1-1")

# 시간 복잡도 O(2^n) : 매번 left, righ 2개의 재귀가 실행
# 공간 복잡도 O(2^n) : 최악의 경우 모든 결과 저장 가능