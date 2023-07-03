# 스택 이용 풀이 - 통과 (아래 풀이와 시간은 큰 차이 나지 않음)

p = input()

stack = []

result = 0

for i in range(len(p)):
    if p[i] == '(':
        stack.append('(')

    else:
        if p[i - 1] == '(':     # 입력값으로 이전 값 확인
            stack.pop()
            result += len(stack)

        else:
            stack.pop()
            result += 1

print(result)

# # 스택을 생각하긴 했지만.. 애매한 풀이 (스택의 특성을 이용하지 않았다고 생각함) - 통과
# p = input()
#
# stack = []
# nums = 0
#
# result = 0
#
# for i in p:
#
#     if i == '(':
#         nums += 1
#
#     else:
#         if stack[-1] == '(':
#             nums -= 1
#             result += nums
#         else:
#             nums -= 1
#             result += 1
#
#     stack.append(i)
#
# print(result)