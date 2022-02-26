from sys import stdin
input = stdin.readline

string = input()

for i in range(len(string)):
    if string[i] == "U": 
        for j in range(i+1, len(string)):
            if string[j] == "C":
                for k in range(j+1, len(string)):
                    if string[k] == "P":
                        for h in range(k+1, len(string)):
                            if string[h] == "C":
                                print("I love UCPC")
                                exit(0)

print("I hate UCPC")
