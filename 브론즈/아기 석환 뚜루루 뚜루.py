N = int(input())

words = ["baby","sukhwan","tururu","turu","very","cute","tururu","turu","in","bed","tururu","turu","baby","sukhwan"]

for i in range(N):
    if "turu" in words[i % 14] and i == N-1: 
        words[i % 14] += "ru" * int(i / 14)
    if i == N-1: 
        #print(words[i%14])
        cnt = words[i%14].count("ru")
        if  cnt >= 5: 
            print("tu+ru*",cnt, sep="")
            
        else: print(words[i%14])
