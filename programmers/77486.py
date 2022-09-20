import collections
def solution(enroll, referral, seller, amount):
    match = collections.defaultdict(list)
    result = [0] * len(enroll)

    for i in range(len(enroll)):
        match[enroll[i]].append(referral[i])
        match[enroll[i]].append(i)

    def check(name, money):
        ref, idx = match[name]
        if money == 0:
            return money
        if ref == '-':
            result[idx] += (money - money // 10)
            return money

        result[idx] += (money - check(ref, money // 10))

        return money

    for s in range(len(seller)):
        check(seller[s], amount[s] * 100)

    return result

# 주의!!!!
# 1. round(money * 0.1) 와 같이 처리할 경우 테스트 케이스 통과 x -> 10프로 분배한다는 점에 집중! 반내림, 반올림 상관x
# 2. 재귀는 1000번으로 제한되어있음 -> 사람수가 최대 10000개 일 수 있기 때문에 재귀에 한계가 걸려 처리 x
#   -> money가 0인 경우 바로 return 되도록 처리해야함(추천자가 없는 경우까지 확인할 필요 없도록)