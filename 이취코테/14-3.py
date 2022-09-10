# 내풀이 - 런타임에러
import collections
def solution(N, stages):
    length = len(stages)
    data = collections.Counter(stages)
    rates = []
    for i in range(1, N + 1):
        length -= data[i - 1]
        rate = data[i] / length
        rates.append((i, rate))

    rates.sort(key = lambda x: (-x[1], x[0]))

    answer = []
    for i in rates:
        answer.append(i[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# 책 풀이
def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda t:t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer

# 책 풀이 참고하여 개선한 풀이
import collections
def solution(N, stages):
    length = len(stages)
    data = collections.Counter(stages)
    rates = []
    for i in range(1, N + 1):
        if length == 0:
            rate = 0
        else:
            rate = data[i] / length

        length -= data[i]
        rates.append((i, rate))

    rates.sort(key = lambda x: -x[1])

    answer = [i[0] for i in rates]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

