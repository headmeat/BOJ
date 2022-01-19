A = int(input())
B = int(input())
C = int(input())

res = str(A * B * C)

for i in "0123456789":
    print(res.count(i))
