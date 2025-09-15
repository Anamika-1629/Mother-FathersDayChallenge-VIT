class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        val = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return val

    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        val = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return val

    def empty(self):
        return len(self.s1) == 0

def main():
    q = MyQueue()
    q.push(1)
    q.push(2)
    print("Peek:", q.peek())  
    print("Pop:", q.pop())    
    print("Empty:", q.empty())

if __name__ == "__main__":
    main()
