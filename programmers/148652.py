def solution(n, l, r):
    def count_bit_1(num):
        if num <= 5: return '11011'[:num].count('1')

        base = 1
        while 5 ** (base + 1) < num:
            base += 1

        section = num // (5 ** base)
        remainder = num % (5 ** base)

        answer = section * (4 ** base)

        if section >= 3:
            answer -= (4 ** base)

        if section == 2:
            return answer
        else:
            return answer + count_bit_1(remainder)

    return count_bit_1(r) - count_bit_1(l - 1)

s = solution(2, 4, 17)
print(s)

# 참고 https://school.programmers.co.kr/questions/41641