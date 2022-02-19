from sys import stdin
input = stdin.readline

menu = []

def main():
    n, q = map(int, input().split())

    for _ in range(n):
        a, b = map(int, input().split())
        menu.append((a, b))

    menu.sort(key = lambda x: x[0])

    for _ in range(q):
        u, v, x, y = map(int, input().split())
        front, back = binarySearch(u, v, menu, 0)
        cnt = 0

        for i in menu[front:back + 1]:
            if i[1] >= x and i[1] <= y: cnt += 1
        
        print(cnt)

def binarySearch(a, b, lst, key):
    left, right = 0, len(lst) - 1
    front = -1

    while(left <= right):
        mid = (left + right) // 2

        if lst[mid][key] == a:
            front = mid
            sw = True
            break
        elif lst[mid][key] < a:
            left = mid + 1
        else:
            right = mid - 1

    if front == -1: front = left

    left, right = 0, len(lst) - 1
    back = -1

    while(left <= right):
        mid = (left + right) // 2

        if lst[mid][key] == b:
            back = mid
            break
        elif lst[mid][key] < b:
            left = mid + 1
        else:
            right = mid - 1
    
    if back == -1: back = right

    return front, back

if __name__ == '__main__':
    main()
