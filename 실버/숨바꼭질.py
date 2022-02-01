from collections import deque
soobin, bro = map(int, input().split())
queue = deque()
cnt = 1

visited = [0 for i in range(100001)]

queue.append((soobin, cnt))
visited[soobin] = 1
tmp = (-1, -1)

while( soobin != bro ):
    tmp = queue.popleft()
    prev = tmp[1]
    soobin = tmp[0]

    if soobin -1 >= 0 and visited[soobin-1] == 0:
        queue.append((soobin - 1, prev + 1))
        visited[soobin - 1] = 1
    if soobin + 1 < 100001 and visited[soobin+1] == 0:
        queue.append((soobin + 1, prev + 1))
        visited[soobin + 1] = 1
    if soobin * 2 < 100001 and visited[soobin*2] == 0:
        queue.append((soobin * 2, prev + 1))
        visited[soobin * 2] = 1

if tmp[1] >=1: print(tmp[1] - 1)
else: print(0)
  
#스쳐 지나간 아이디어도 신중히
#https://chanhuiseok.github.io/posts/baek-14/
