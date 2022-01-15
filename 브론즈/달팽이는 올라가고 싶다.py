A, B, V = map(int, input().split())
tmp = -1

if int((V-A) / (A-B)) < (V-A) / (A-B):
    tmp = int((V-A) / (A-B)) * (A-B) +(A-B)
else: tmp = int((V-A) / (A-B)) * (A-B)

print(int(tmp / (A-B)) + 1)
