n = int(input())
cnt = 0

for _ in range(n):
    string = input()
    sw = True
    prev = string[0]
    arr = [0 for _ in range(26)]

    for i in range(len(string)):
        if prev != string[i]:
            if arr[ord(string[i]) - 97] != 0: 
                sw = False
                break
        arr[ord(string[i]) - 97] = 1
        prev = string[i]
    if sw == True: cnt += 1

print(cnt)
