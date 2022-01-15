A, B = input().split()

#최대 연속해서 일치하는 개수

mx = len(B)+1
for i in range(len(B)):
    if i + len(A) > len(B): break
    sm = 0 
    for j in range(len(A)):
        if A[j] != B[i:i+len(A)][j]:
            sm += 1
    mx = min(mx, sm)

print(mx)
