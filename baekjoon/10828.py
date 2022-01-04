# 시간초과 해결
# 줄바꿈을 입력으로 처리하기 때문에 strip() 사용해서 처리 필요
import sys
input=sys.stdin.readline

n = int(input())

class Stack:
    def __init__(self):
        self.result = []

    def push(self, num):
        self.result.append(num)

    def pop(self):
        if not self.result:
            return -1
        return self.result.pop()

    def size(self):
        return len(self.result)

    def empty(self):
        if not len(self.result):
            return 1
        return 0

    def top(self):
        if not self.result:
            return -1
        return self.result[-1]


stack = Stack()
for i in range(n):
    orders = input().split().strip()
    order = orders[0]
    if order == 'push':
        stack.push(orders[1])
    elif order == 'pop':
        print(stack.pop())
    elif order == 'size':
        print(stack.size())
    elif order == 'empty':
        print(stack.empty())
    elif order == 'top':
        print(stack.top())

