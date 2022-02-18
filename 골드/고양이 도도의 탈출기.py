from sys import stdin
import heapq
input = stdin.readline

INF = 10 ** 10
n, m = map(int, input().split())
arr = [[x for x in input().rstrip()] for _ in range(n)]
dist = [[INF for i in range(m)] for _ in range(n)]
life = {"L":5, "F":1, "X":10}

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "C": 
            start = (i, j)
            dist[i][j] = 0
        elif arr[i][j] == "E": end = (i, j)

queue = []

heapq.heappush(queue, (0, start))

while(queue):
    distance, location = heapq.heappop(queue)
    now = arr[location[0]][location[1]]

    if dist[location[0]][location[1]] < distance: continue

    neighbors = []

    if location[0] + 1 < n and arr[location[0] + 1][location[1]] != "D":
        if now == "X":
            health_minus = 0 if arr[location[0] + 1][location[1]] == "X" else 10
            neighbors.append((health_minus, (location[0] + 1, location[1])))
        elif arr[location[0] + 1][location[1]] == "L":
            neighbors.append((life["L"], (location[0] + 1, location[1])))
    if now != "X":
        if location[0] - 1 >= 0 and arr[location[0]][location[1]] == "L" and arr[location[0] - 1][location[1]] != "D":
            neighbors.append((life["L"], (location[0]-1, location[1])))
        if location[1] + 1 < m and arr[location[0]][location[1] + 1] != "D":
            neighbors.append((life["F"], (location[0], location[1]+1)))
        if location[1] - 1 >= 0 and arr[location[0]][location[1] - 1] != "D":
            neighbors.append((life["F"], (location[0], location[1]-1)))

    for t in neighbors:
        w, wichi = t

        if w + distance < dist[wichi[0]][wichi[1]]:
            dist[wichi[0]][wichi[1]] = w + distance
            heapq.heappush(queue, (w + distance, wichi))

answer = dist[end[0]][end[1]]
if answer == INF: print("dodo sad")
else: print(answer)
