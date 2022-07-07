from sys import stdin
import heapq
input = stdin.readline

for _ in range(int(input())):
    k = int(input())
    dic = {}
    maxq = []
    minq = []

    for _ in range(k):
        op, num = input().split()
        num = int(num)
        if op=="I":
            if num not in dic.keys(): dic[num] = 0
            dic[num] += 1
            heapq.heappush(maxq, -num)
            heapq.heappush(minq, num)
        elif num==-1:
            while(minq):
                tmp = heapq.heappop(minq)
                if dic[tmp]>0:
                    dic[tmp] -= 1
                    break
        else:
            while(maxq):
                tmp = -heapq.heappop(maxq)
                if dic[tmp]>0:
                    dic[tmp] -= 1
                    break
    cnt = 0

    while(maxq):
        tmp = -heapq.heappop(maxq)
        if dic[tmp]>0:
            print(tmp, end = " ")
            cnt += 1
            break

    while(minq):
        tmp = heapq.heappop(minq)
        if dic[tmp]>0:
            print(tmp)
            cnt += 1
            break

    if cnt==0: print("EMPTY")
