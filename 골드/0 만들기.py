from sys import stdin
input = stdin.readline

t = int(input())
ops = ["+", "-", " "]
ans = 0

def calc(arr):
    global ans
    tmp = []
    num = ""
    
    for i in range(len(arr)):
        if arr[i]=="+" or arr[i]=="-":
            tmp.append(num)
            tmp.append(arr[i])
            num = ""
        elif arr[i] == " ": continue
        else: num += arr[i]

    tmp.append(num)
    
    res = int(tmp[0])
    idx = 1

    while(idx<len(tmp)):
        if tmp[idx] == "+": 
            idx += 1
            res += int(tmp[idx])
            idx += 1
        elif tmp[idx] == "-": 
            idx += 1
            res -= int(tmp[idx])
            idx += 1

    if res: return False
    else: return True

def solve(arr, n, k, hole):
    if k==n:
        arr += str(n+1)
        if calc(arr): hole.append("".join(arr))
        return
    
    for i in range(3):
        arr += str(k+1)+ops[i]
        solve(arr, n, k+1, hole)
        arr = arr[:-2]

for i in range(t):
    hole = []
    solve("", int(input())-1, 0, hole)
    hole.sort()
    print("\n".join(hole)+"\n")
