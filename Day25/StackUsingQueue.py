class MyStack(object):
    def __init__(self):
        self.q1 = []
        self.q2 = []
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        return self.q1.pop(0)
    def top(self):
        return self.q1[0]
    def empty(self):
        return len(self.q1) == 0

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print("Top:", stack.top())
    print("Pop:", stack.pop())
    print("Empty:", stack.empty())
