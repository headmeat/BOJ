from collections import deque

N, M, start = map(int, input().split())

edges = [list(map(int, input().split())) for i in range(M)]

def dfs(edges, visited):
    stack = []
    stack.append(start)

    while(len(stack)!=0):
        cur = stack[-1]
        if visited[cur] == False: print(cur, end = " ")
        visited[cur] = True

        for j in edges:
            if cur in j:
                cur_idx = j.index(cur)
                nei_idx = 0 if cur_idx == 1 else 1
                neigh = j[nei_idx]
                if visited[neigh] == False:
                    stack.append(neigh)
                    break
            if j == edges[-1]: stack.pop()

def bfs(edges, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    print(start, end = " ")

    while(len(queue)!=0):
        cur = queue.popleft()

        for j in edges:
            if cur in j:
                cur_idx = j.index(cur)
                nei_idx = 0 if cur_idx == 1 else 1
                neigh = j[nei_idx]
                if visited[neigh] == False:
                    queue.append(neigh)
                    visited[neigh] = True
                    print(neigh, end = " ")

for i in edges:
    if i[0] > i[1]:
        tmp = i[0]
        i[0] = i[1]
        i[1] = tmp
edges.sort(key=lambda x: (x[0], x[1]))

visited = [False for i in range(N+1)]
dfs(edges, visited)

print()

visited = [False for i in range(N+1)]
bfs(edges, visited)
