from collections import defaultdict

def solution(weights):
    result = 0

    weight = defaultdict(int)

    for w in weights:
        result += weight[w] + weight[w*2] + weight[w/2] + weight[(w*2)/3] + weight[(w*3)/2] + weight[(w*4)/3] + weight[(w*3)/4]

        weight[w] += 1

    return result

# from collections import defaultdict
#
#
# def solution(weights):
#     set_weights = list(set(weights))
#     set_weights.sort()
#
#     result = len(weights) - len(set_weights)
#
#     weight = defaultdict(int)
#     mul = [2, 3, 4]
#
#     for w in set_weights:
#         for m in mul:
#             result += weight[w * m]
#
#             weight[w * m] += 1
#
#     return result
#
# s = solution([100,180,180,360,100,270])
# print(s)