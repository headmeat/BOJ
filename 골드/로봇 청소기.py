from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[0 for _ in range(m)] for _ in range(n)]
count = 0
#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#북동남서 각각의 왼쪽 방향
directions = [3,0,1,2]

def clean(v, d):
    global count

    while(True):
        sw = False
        cleaned[v[0]][v[1]] = 1

        for i in range(4):
            d = directions[d]
            x = v[0]+dx[d]
            y = v[1]+dy[d]

            if 0<=x<n and 0<=y<m and cleaned[x][y] == 0 and arr[x][y] == 0:
                count += 1
                sw = True
                v[0], v[1] = x, y
                break

        if sw == False:
            a = v[0]
            b = v[1]

            if d==0 or d==2:
                a = v[0]+dx[(d+2)%4]
            else:
                b = v[1]+dy[(d+2)%4]
            
            if arr[a][b] == 1:
                print(count)
                exit(0)
            elif 0<=a<n and 0<=b<m:
                v[0], v[1] = a, b

count += 1
clean([r, c], d)
