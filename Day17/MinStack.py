class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

def main():
    minStack = MinStack()
    n = int(input("Enter number of operations: "))
    for _ in range(n):
        op = input("Operation (push x / pop / top / getMin): ").split()
        if op[0] == "push":
            minStack.push(int(op[1]))
        elif op[0] == "pop":
            minStack.pop()
        elif op[0] == "top":
            print("Top:", minStack.top())
        elif op[0] == "getMin":
            print("Min:", minStack.getMin())

if __name__ == "__main__":
    main()
