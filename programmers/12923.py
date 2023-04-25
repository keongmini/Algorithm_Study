# 시간 초과
def solution(begin, end):
    result = []

    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
            continue

        flag = True
        for j in range(2, int(i ** 1 / 2) + 1):
            if i % j == 0 and i // j <= 10000000:
                flag = False
                result.append(i // j)
                break

        if flag:
            result.append(1)

    return result


# 참고. https://ye0nn.tistory.com/41 (최대 약수 구하기)