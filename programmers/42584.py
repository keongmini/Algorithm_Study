# def solution(prices):
#     answer = []
#     idx = 0
#     for price in prices:
#         cnt = 0
#         for i in range(idx+1, len(prices)):
#             cnt += 1
#             if price > prices[i]:
#                 break
#         answer.append(cnt)
#         idx += 1
#
#     return answer

def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer

s = solution([1, 2, 3, 2, 3])
print(s)