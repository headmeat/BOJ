from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0

#0: 가로, 1: 세로

def before(i, j, l, plane, visited):
    if plane == 0:
        for k in range(j, j-l, -1):
            if not (0<=k<n and arr[i][k]==arr[i][j] and visited[k]==0):
                return False

        for k in range(j, j-l, -1):
            visited[k] += 1
    else:
        for k in range(i, i-l, -1):
            if not (0<=k<n and arr[k][j]==arr[i][j] and visited[k]==0):
                return False

        for k in range(i, i-l, -1):
            visited[k] += 1

    return True

def after(i, j, l, plane, visited):
    if plane == 0:
        for k in range(j, j+l):
            if not (0<=k<n and arr[i][k]==arr[i][j] and visited[k]==0):
                return False

        for k in range(j, j+l):
            visited[k] += 1
    else:
        for k in range(i, i+l):
            if not (0<=k<n and arr[k][j]==arr[i][j] and visited[k]==0):
                return False
        
        for k in range(i, i+l):
            visited[k] += 1
    
    return True

for i in range(n):
    visited = [0 for _ in range(n)]
    for j in range(0, n-1):
        if arr[i][j] < arr[i][j+1]:
            if before(i, j, l, 0, visited) and arr[i][j]+1==arr[i][j+1]:
                continue
            else: 
                count -= 1
                break
        elif arr[i][j] > arr[i][j+1]:
            if after(i, j+1, l, 0, visited) and arr[i][j]-1==arr[i][j+1]:
                continue
            else:
                count -= 1
                break
    count += 1

    visited = [0 for _ in range(n)]
    for j in range(0, n-1):
        if arr[j][i] < arr[j+1][i]:
            if before(j, i, l, 1, visited) and arr[j][i]+1==arr[j+1][i]:
                continue
            else: 
                count -= 1
                break
        elif arr[j][i] > arr[j+1][i]:
            if after(j+1, i, l, 1, visited) and arr[j][i]-1==arr[j+1][i]:
                continue
            else:
                count -= 1
                break

    count += 1

#[1, 0, 1, 0, 0, 0]
print(count)
