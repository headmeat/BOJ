from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
lst = [[x for x in input().rstrip()] for _ in range(n)]

def solve(arr, red, blue):
    for k in range(4):
        if len(arr) > 0 and arr[-1] == k: continue

        tred, tblue = list(red), list(blue)
        red_stop = True
        blue_stop = True

        if k == 0:#상
            while( True ):
                sw = True

                if red_stop and tred[0] - 1 >= 0 and lst[tred[0] - 1][tred[1]] != "#" and [tred[0]-1, tred[1]] != tblue:
                    tred[0] -= 1
                    sw = False
                if tblue[0] - 1 >= 0 and lst[tblue[0] - 1][tblue[1]] != "#" and ([tblue[0]-1, tblue[1]] != tred or not red_stop):
                    tblue[0] -= 1
                    sw = False

                if tblue == hole: 
                    blue_stop = False
                    break
                if tred == hole:
                    red_stop = False
                    if sw == True:
                        print("1")
                        exit(0)

                if sw == True: break
        elif k == 1:#하
            while(True):
                sw = True

                if red_stop and tred[0] + 1 < n and lst[tred[0] + 1][tred[1]] != "#" and [tred[0]+1, tred[1]] != tblue:
                    tred[0] += 1
                    sw = False
                if tblue[0] + 1 < n and lst[tblue[0] + 1][tblue[1]] != "#" and ([tblue[0]+1, tblue[1]] != tred or not red_stop):
                    tblue[0] += 1
                    sw = False

                if tblue == hole: 
                    blue_stop = False
                    break
                if tred == hole:
                    red_stop = False
                    if sw == True:
                        print("1")
                        exit(0)

                if sw == True: break
        elif k == 2:#좌
            while(True):
                sw = True

                if red_stop and tred[1] - 1 >= 0 and lst[tred[0]][tred[1] - 1] != "#" and [tred[0], tred[1] - 1] != tblue:
                    tred[1] -= 1
                    sw = False
                if tblue[1] - 1 >= 0 and lst[tblue[0]][tblue[1] - 1] != "#" and ([tblue[0], tblue[1] - 1] != tred or not red_stop):
                    tblue[1] -= 1
                    sw = False

                if tblue == hole: 
                    blue_stop = False
                    break
                if tred == hole:
                    red_stop = False
                    if sw == True:
                        print("1")
                        exit(0)

                if sw == True: break
        else:#우
            while(True):
                sw = True

                if red_stop and tred[1] + 1 < m and lst[tred[0]][tred[1] + 1] != "#" and [tred[0], tred[1] + 1] != tblue:
                    tred[1] += 1
                    sw = False
                if tblue[1] + 1 < m and lst[tblue[0]][tblue[1] + 1] != "#" and ([tblue[0], tblue[1] + 1] != tred or not red_stop):
                    tblue[1] += 1
                    sw = False

                if tblue == hole: 
                    blue_stop = False
                    break
                if tred == hole:
                    red_stop = False
                    if sw == True:
                        print("1")
                        exit(0)

                if sw == True: break

        if blue_stop == True:
            arr.append(k)
            if len(arr) < 10: solve(arr, tred, tblue)
            del arr[-1]

red = blue = hole = -1

for i in range(len(lst)):
    if "R" in lst[i]: red = [i, lst[i].index("R")]
    if "B" in lst[i]: blue = [i, lst[i].index("B")]
    if "O" in lst[i]: hole = [i, lst[i].index("O")]

solve([], red, blue)

print(0)
