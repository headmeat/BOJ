from sys import stdin
import heapq
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = []

    for i in range(n//10 + 1):
        arr += list(map(int, input().split()))

    minheap, maxheap = [], []
    ans = []

    for i in range(len(arr)):
        if len(minheap)==0:
            heapq.heappush(minheap, -arr[i])
        elif len(minheap)==len(maxheap):
            if arr[i]>maxheap[0]:
                heapq.heappush(minheap, -heapq.heappop(maxheap))
                heapq.heappush(maxheap, arr[i])
            else: heapq.heappush(minheap, -arr[i])
        elif len(minheap)>len(maxheap):
            if arr[i] > -minheap[0]:
                heapq.heappush(maxheap, arr[i])
            else:
                heapq.heappush(maxheap, -heapq.heappop(minheap))
                heapq.heappush(minheap, -arr[i])

        if i % 2 == 0: ans.append(-minheap[0])

    print(len(ans))

    for i in range(len(ans)):
        if i%10==0 and i!=0: print()
        print(ans[i], end = " ")

    print()
