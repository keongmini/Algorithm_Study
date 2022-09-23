import string

# 10진수 -> n진수 변환
tmp = string.digits + string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    num = str(convert(n, k))

    cnt = 0
    if '0' not in num:
        if prime(int(num)):
            cnt += 1

    else:
        for i in num.split('0'):
            if i.isdigit():
                if int(i) > 2 and prime(int(i)):
                    cnt += 1
                elif int(i) == 2:
                    cnt += 1

    return cnt