# wrong answer
class MyCircularQueue(object):
    def __init__(self, k):
        self.queue = [None for i in range(k)]
        self.front = 0
        self.rear = 0
        self.index = 0

    def enQueue(self, value):
        if not self.isFull():
            if self.isEmpty():
                self.front = value
            self.queue[self.index] = value
            self.index += 1
            if self.index >= len(self.queue):
                self.index = 0
            self.rear = value
            return True
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            for i, v in enumerate(self.queue):
                if v == self.front:
                    self.queue[i] = 0
                    if i >= len(self.queue) - 1:
                        self.front = self.queue[0]
                    else:
                        self.front = self.queue[i + 1]
                    return True
        return False

    def Front(self):
        if self.isEmpty():
            return -1
        return self.front

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.rear

    def isEmpty(self):
        for value in self.queue:
            if value:
                return False
        return True

    def isFull(self):
        for value in self.queue:
            if not value:
                return False
        return True

# answer
class MyCircularQueue(object):
    def __init__(self, k):
        self.q = [None for i in range(k)]
        self.maxlen = k
        self.p1 = 0     # front index
        self.p2 = 0     # rear index

    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen   # 리스트 인덱스와 맞추기 위해
            return True

    def Front(self):
        if self.q[self.p1] is None:
            return -1
        else:
            return self.q[self.p1]

    def Rear(self):
        if self.q[self.p2 - 1] is None:
            return -1
        else:
            return self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None