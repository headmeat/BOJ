#S = input()
S = "".join([str(x) for x in range(8,1005)])

first = -1

t = 0
tupac = 0

while(t <= int(len(S)/2)):
    cnt = 0
    for i in range(1, int(len(S)/2)+1):
        tupac += 1
        if tupac >= 10: raise Exception()
        fst = int(S[i:i+t+1])
        sec = int(S[i+t+1:2*i+t+1])
        print("#1",fst, sec)
        if fst >= sec: break
        if fst + 1 != sec: cnt += 1
        if cnt == 2: 
            first = fst - 1
            break
    if first != -1: break
    else: t += 1
    

if first != -1:
    i = 0
    digits = -1
    L = len(str(first))
    print("L:",L)
    print("S:", len(S))
    while i < len(S):
        tmp = int("9"*L)

        if digits == -1:
            i += (tmp - first + 1) * L
        else:
            k = int("1"+"0"*(L-1))
            i += (tmp - k + 1) * L            

        print(i)
        digits = L
        L += 1
    
    print(first, S[-digits:])
else: print(S, S)
