import sys
input = sys.stdin.readline

n = int(input())

class Queue:
    def __init__(self):
        self.result = []

    def push(self, num):
        self.result.append(num)

    def pop(self):
        if not self.result:
            return -1
        return self.result.pop(0)

    def size(self):
        return len(self.result)

    def empty(self):
        if not self.result:
            return 1
        return 0

    def front(self):
        if not self.result:
            return -1
        return self.result[0]

    def back(self):
        if not self.result:
            return -1
        return self.result[-1]

queue = Queue()

for _ in range(n):
    orders = input().split()
    order = orders[0]

    if order == 'push':
        queue.push(orders[1])
    elif order == 'pop':
        print(queue.pop())
    elif order == 'size':
        print(queue.size())
    elif order == 'empty':
        print(queue.empty())
    elif order == 'front':
        print(queue.front())
    elif order == 'back':
        print(queue.back())