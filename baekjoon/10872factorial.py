
# 1번 풀이 - for문
number = int(input())

num = 1
for i in range(number, 0, -1):
    if i != 0:
        num *= i

print(num)

# 2번 풀이 - 재귀함수
number = int(input())

def factorial(num):
    if num != 0:
        return num * factorial(num-1)
    elif num == 0:
        return 1

print(factorial(number))