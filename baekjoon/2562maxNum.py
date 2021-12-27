numList = [int(input()) for i in range(9)]

# 1번 풀이 - enumerate
# maxIdx = 0
# maxNum = 0
# for idx, num in enumerate(numList):
#     if num > maxNum:
#         maxNum = num
#         maxIdx = idx+1
#
# print(maxNum)
# print(maxIdx)

# 2번 풀이 - 내장함수 사용
print(max(numList))
print(numList.index(max(numList))+1)