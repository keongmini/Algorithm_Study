class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            
            while stack and stack[-1][0] < t:
                tem, idx = stack.pop()
                result[idx] = i - idx
            
            stack.append((t, i))
        
        return result
