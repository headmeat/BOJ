N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = []

idx_A = 0
idx_B = 0

while(True):
    if idx_A>=len(A):
        for i in range(idx_B, len(B)): 
            res.append(B[i])
        break
    if idx_B>=len(B):
        for i in range(idx_A, len(A)): 
            res.append(A[i])
        break

    if A[idx_A] <= B[idx_B]:
        res.append(A[idx_A])
        idx_A += 1
    else:
        res.append(B[idx_B])
        idx_B += 1

print(" ".join(map(str, res)))
