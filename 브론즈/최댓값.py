import sys

lst = []

for i in range(9):
    lst.append(int(sys.stdin.readline().rstrip()))

val = max(lst)
print(val, lst.index(val)+1)
