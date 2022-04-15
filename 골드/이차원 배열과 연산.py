from sys import stdin
input = stdin.readline

r,c,k=map(int,input().split())
arr=[]
b=-1
for _ in range(3):
    arr.append(list(map(int,input().split())))
    b=max(b,max(arr[_]))

def row_call():
    global arr
    mx=0

    for i in range(len(arr)):
        count=[[j,0] for j in range(101)]
        for j in arr[i]:
            if j==0: continue
            count[j][1]+=1
        count.sort(key=lambda x: (x[1],x[0]))
        arr[i]=[]
        
        for j in range(len(count)):
            if len(arr[i])>=100: break
            if count[j][1]==0: continue
            arr[i].append(count[j][0])
            arr[i].append(count[j][1])
        mx=max(mx,len(arr[i]))
    
    for i in range(len(arr)):
        for j in range(mx-len(arr[i])):
            arr[i].append(0)

def col_call():
    global arr
    mx=0
    stack=[[] for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        count=[[j,0] for j in range(101)]
        for j in range(len(arr)):
            if arr[j][i]==0: continue
            count[arr[j][i]][1]+=1
        count.sort(key=lambda x: (x[1],x[0]))
        for j in range(len(count)):
            if len(stack[i])>=100: break
            if count[j][1]==0: continue
            stack[i].append(count[j][0])
            stack[i].append(count[j][1])
        mx=max(mx,len(stack[i]))
    tmp_arr=[[] for _ in range(mx)]
    for i in range(len(stack)):
        for j in range(mx):
            if j<len(stack[i]):
                tmp_arr[j].append(stack[i][j])
            else: tmp_arr[j].append(0)
    arr=tmp_arr

for t in range(101):
    if 0<=r-1<len(arr) and 0<=c-1<len(arr[0]) and arr[r-1][c-1]==k:
        print(t)
        exit(0)

    row=len(arr)
    col=len(arr[0])

    if row>=col:
        row_call()
    else:
        col_call()

print(-1)
