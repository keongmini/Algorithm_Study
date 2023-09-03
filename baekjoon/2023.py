# 참고 https://yanoo.tistory.com/48

N = int(input())


def isPrime(num):                               # 소수인지 확인용 함수
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def check(now):
    if len(str(now)) == N:          # 길이 도달
        print(now)
        return

    for i in range(10):             # 숫자 하나씩 붙여주기
        tmp = now * 10 + i
        if isPrime(tmp):
            check(tmp)


# 한자리 수 중에 소수인 숫자로 시작
check(2)
check(3)
check(5)
check(7)