from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robots = [-1 for _ in range(n)]
broken = [0 for _ in range(2*n)]
count = 0

def rotate():
    global belt, robots, broken
    belt = [belt[2*n-1]] + belt[:2*n-1]
    robots = [-1] + robots[:n-1]
    broken = [broken[2*n-1]] + broken[:2*n-1]

def move():
    for i in range(n-1, -1, -1):
        if robots[i]==-1: continue

        if i+1==n: robots[i] = -1
        elif i+1<n and robots[i+1]==-1 and belt[i+1]>0:
            robots[i+1] = 1
            robots[i] = -1
            belt[i+1] -= 1
            if belt[i+1]==0: broken[i+1] = 1

def put():
    if belt[0]>0:
        belt[0] -= 1
        if belt[0] == 0: broken[0] = 1
        robots[0] = 1

while(sum(broken)<k):
    count += 1
    rotate()
    move()
    put()

print(count)
