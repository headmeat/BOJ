from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
shark = [n//2, n//2]
score = [0, 0, 0]

arr = [list(map(int, input().split())) for _ in range(n)]
arr[shark[0]][shark[1]] = -1
blizzard = [list(map(int, input().split())) for _ in range(m)]
tmp = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
scroll_x = [0, 1, 0, -1]
scroll_y = [-1, 0, 1, 0]

def color():
    x, y = shark
    sw = 0
    stack = []
    count = 0

    for j in range(1, n):#제한 칸 수
        for k in range(3):#방향 전환
            if j<n-1 and k==2: continue
            for _ in range(j):#실제 이동
                x += scroll_x[sw]
                y += scroll_y[sw]
                count += 1
                tmp[x][y] = count
                
                if arr[x][y]: stack.append(arr[x][y])
                else: break
            sw = (sw + 1)%4
            if arr[x][y] == 0: break
        if arr[x][y] == 0: break
    count = 0
    l = h = 0
    answer = deque()

    while(h<len(stack)):
        if stack[l]==stack[h]:
            count += 1
            h += 1
            if h==len(stack):
                answer.append(count)
                answer.append(stack[l])
        else:
            answer.append(count)
            answer.append(stack[l])
            count = 0
            l = h

    x, y = shark
    sw = 0

    for j in range(1, n):#제한 칸 수
        for k in range(3):#방향 전환
            if j<n-1 and k==2: continue
            for _ in range(j):#실제 이동
                x += scroll_x[sw]
                y += scroll_y[sw]
                
                if answer: arr[x][y] = answer.popleft()
                else: return

            sw = (sw + 1)%4
    
def check():
    global tmp
    ddx = [0, 1, 0, -1]
    ddy = [1, 0, -1, 0]
    x = y = start = sw = 0

    for j in range(n-1, 0, -1):#제한 칸 수
        for k in range(3):#방향 전환
            if j<n-1 and k==2: continue
            for _ in range(j):#실제 이동
                if start and arr[x][y]==0: return True
                if arr[x][y]: start = 1
                x += ddx[sw]
                y += ddy[sw]

            sw = (sw + 1)%4

    return False

def storm(d, s):
    x, y = shark

    for i in range(1, s+1):
        #if arr[x+dx[d]*i][y+dy[d]*i]>0: score[arr[x+dx[d]*i][y+dy[d]*i]-1] += 1
        arr[x+dx[d]*i][y+dy[d]*i] = 0

    return

def pop():
    x, y = shark
    q = deque()
    sw = 0

    for j in range(1, n):#제한 칸 수
        for k in range(3):#방향 전환
            if j<n-1 and k==2: continue
            for _ in range(j):#실제 이동
                x += scroll_x[sw]
                y += scroll_y[sw]
                
                if arr[x][y]: 
                    q.append(arr[x][y])
                    arr[x][y] = 0

            sw = (sw + 1)%4

    x, y = shark
    sw = 0

    for j in range(1, n):
        for k in range(3):
            if j<n-1 and k==2: continue
            for _ in range(j):
                x += scroll_x[sw]
                y += scroll_y[sw]
                if len(q)>0: arr[x][y] = q.popleft()
                else: break
            
            sw = (sw + 1)%4
        
        if len(q)==0: break

def consec():
    x, y = shark
    sw = 0
    stack = []

    for j in range(1, n):
        for k in range(3):
            if j<n-1 and k==2: continue
            for _ in range(j):
                x += scroll_x[sw]
                y += scroll_y[sw]
                if stack:
                    a, b = stack[-1]
                    if arr[a][b]==arr[x][y]: stack.append((x, y))
                    else: 
                        if len(stack)>=4:
                            score[arr[a][b]-1] += len(stack)
                            while(stack):
                                a, b = stack.pop()
                                arr[a][b] = 0

                        stack = []
                        stack.append((x, y))
                else: stack.append((x, y))
            
            sw = (sw + 1)%4

    return

for i in range(m):
    d, s = blizzard[i]
    storm(d-1, s)

    x, y = shark
    q = deque()
    sw = 0

    while(check()): 
        pop()
        consec()

    color()

ans = 0

for i in range(1, 4):
    ans += score[i-1]*i

print(ans)
