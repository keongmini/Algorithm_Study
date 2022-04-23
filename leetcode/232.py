class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        # 큐를 구현 -> 큐는 앞에 있는 값부터 빼야 함
        # 뒤집게 되면 맨 앞에 있는 값이 맨 뒤로 가게 됨 -> 스택처럼 뒤에서 값을 빼도 값은 큐처럼 앞에 있는 값이 빠지는 것처럼 출력
        # 계속 뒤에서 값이 들어오고 나가는 건 앞에서 나가는 거니까 output에 값이 다 없어질 때까지 업데이트 해주지 않아도됨

    def empty(self):
        return self.input == [] and self.output == []