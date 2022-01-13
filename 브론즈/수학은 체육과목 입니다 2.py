N = int(input())

if int(N/4) != N/4: start = int(N/4) * 4 + 1
else: start = N - 3

pat_no = int((N-1)/4)

if pat_no % 2 == 0: print(N - start + 1)
else: print(5 - (N-start))
