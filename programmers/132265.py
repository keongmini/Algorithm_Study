# 같은 풀이 - 실행속도 : 리스트 < 딕샤너리


# 시간초과
# 리스트 이용
# from collections import defaultdict
#
# def solution(topping):
#     result = 0
#
#     nums = defaultdict(int)
#
#     for t in topping:
#         nums[t] += 1
#
#     left = []
#     for t in topping:
#         nums[t] -= 1
#
#         if nums[t] == 0:
#             del nums[t]
#
#         if t not in left:
#             left.append(t)
#
#         if len(left) > len(nums.keys()):
#             break
#
#         if len(left) == len(nums.keys()):
#             result += 1
#
#     return result


# 통과
# 딕셔너리 이용
from collections import defaultdict

def solution(topping):
    result = 0

    left = defaultdict(int)
    right = defaultdict(int)

    for t in topping:
        right[t] += 1

    for t in topping:
        right[t] -= 1

        if right[t] == 0:
            del right[t]

        left[t] += 1

        if len(left) > len(right):
            break

        if len(left) == len(right):
            result += 1

    return result




