class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        result = [-1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                ni, now = stack.pop()
                result[ni] = num

            stack.append((i, num))

        for i, num in enumerate(nums):          # loop 한번더 돌아서 뒤쪽에 있는 값 앞쪽과 비교
            while stack and stack[-1][1] < num:
                ni, now = stack.pop()
                result[ni] = num

        # 통과x - [1,2,3,2,1] => 답: [2,3,-1,3,2] 출력: [2,3,-1,3,3]
        # if stack:
        #     maxNum = max(stack, key=lambda x: x[1])
        #
        #     for i, n in stack:
        #         if n != maxNum[1]:
        #             result[i] = maxNum[1]

        return result

# 개선 풀이 (solution 참고)
# num 까지 stack 에 저장하지 않아도됨 - index 값으로 추정 가능
# for i, num in enumerate(nums):
#     while stack and nums[stack[-1]] < num:
#         res[stack.pop()] = num

# 시간 복잡도: O(n)      스택에 들어가는 요소가 한번씩만 들어가고 나오기 때문에 O(1) 이라 O(n * m)이 아님
# 공간 복잡도: O(n)