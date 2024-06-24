class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        if k > 0:
            stack = stack[:-k]

        result = ''.join(stack).lstrip("0")             # 왼쪽부터 0 제거

        return result if result else "0"                # result = "" 일 경우 처리

# 시간 복잡도 O(N)
# 공간 복잡도 O(N)