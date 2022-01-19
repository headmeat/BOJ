class Stack:
    def __init__(self, size):
        self.size = size
        self.lst = [0 for i in range(size)]

        self.idx = -1

    def push(self, x):
        if self.idx + 1 < self.size:
            self.idx += 1
            self.lst[self.idx] = x

    def pop(self):
        if self.empty(): print("-1")
        else:
            print(self.lst[self.idx])
            self.idx -= 1

    def empty(self):
        if self.idx == -1: 
            return True
        else: 
            return False

    def size1(self):
        print(self.idx + 1)
        #return self.idx + 1

    def top(self):
        if self.empty(): 
            print("-1")
            return False
        else: 
            print(self.lst[self.idx])
            return True

stk = Stack(10000)

N = int(input())
orders = []

for i in range(N):
    inp = input().split()
    if len(inp)>1: orders.append([inp[0], int(inp[1])])
    else: ord = orders.append([inp[0]])

for ord in orders:
    if ord[0] == "push": stk.push(ord[1])
    elif ord[0] == "pop": stk.pop()
    elif ord[0] == "size": stk.size1()
    elif ord[0] == "empty": 
        if stk.empty(): print("1")
        else: print("0")
    elif ord[0] == "top": stk.top()
