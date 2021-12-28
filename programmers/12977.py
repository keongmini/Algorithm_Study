from itertools import combinations

def solution(nums):
    combis = combinations(nums,3)
    caseNum = 0
    for i in combis:
        check = 1
        sumNum = sum(i)
        for j in range(2,sumNum):
            if sumNum % j == 0:
                check = 0
                break
        if check:
            caseNum += 1

    return caseNum

print(solution([1,2,7,6,4]))