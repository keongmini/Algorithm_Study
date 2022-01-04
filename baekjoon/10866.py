import sys
input = sys.stdin.readline

n = int(input())

class Deque:
    def __init__(self):
        self.result = []

    def push_front(self, num):
        self.result.insert(0, num)

    def push_back(self, num):
        self.result.append(num)

    def pop_front(self):
        if not self.result:
            return -1
        return self.result.pop(0)

    def pop_back(self):
        if not self.result:
            return -1
        return self.result.pop()

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

deque = Deque()

for _ in range(n):
    orders = input().split()
    order = orders[0]

    if order == 'push_front':
        deque.push_front(orders[1])
    elif order == 'push_back':
        deque.push_back(orders[1])
    elif order == 'pop_front':
        print(deque.pop_front())
    elif order == 'pop_back':
        print(deque.pop_back())
    elif order == 'size':
        print(deque.size())
    elif order == 'empty':
        print(deque.empty())
    elif order == 'front':
        print(deque.front())
    elif order == 'back':
        print(deque.back())