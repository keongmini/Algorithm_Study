# atoi : 문자열을 정수로 변환
class Solution:
    def myAtoi(self, input: str) -> int:
        sign = 1        # 값의 부호
        result = 0      # 값
        index = 0       # 숫자가 시작되는 인덱스
        n = len(input)

        INT_MAX = pow(2, 31) - 1        # pow(x, y) : x의 y승 지수함수 결과 반환
        INT_MIN = -pow(2, 31)

        # 빈칸 제거
        while index < n and input[index] == ' ':
            index += 1

        # 값의 부호 결정
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1

        # 위에서 빈칸, 값의 부호까지 확인했는데 숫자가 아닌 것이 다른 것이 나온다면 0 출력
        while index < n and input[index].isdigit():
            digit = int(input[index])

            # 해당 조건문 아래에 result에서 10을 곱하고 현재 값을 더해서 결과값을 만들어낼 것이기 때문에 처리 하기 전에
            # 최대값을 10으로 나눈 값과 비교하여 더 크면 최대값보다 크다는 뜻이니 최대/최소값으로 반환 처리
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            # 결과는 숫자로 반환되어야 하지만 현재 처리하고 있는 것은 문자열이기 때문에 이전값의 뒤에 값을 붙여주어야 함
            # 이전 결과 값에 10을 곳하여 1의 자리숫자에 현재 숫자 더하면서 문자열처럼 값이 뒤에 붙여지도록 구현

            index += 1

        return sign * result