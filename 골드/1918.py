from sys import stdin
input = stdin.readline

string = [x for x in input().rstrip()]
stack = []
ans = ""

for i in string:
    if i == "(": stack.append(i)
    elif i == ")":
        while(stack):
            popped = stack.pop()
            if popped=="(": break
            else: ans += popped
    elif i=="+" or i=="-":
        while(stack):
            if stack[-1]=="(": break
            else: ans += stack.pop()
        stack.append(i)
    elif i=="*" or i=="/":
        while(stack):
            if stack[-1]=="*" or stack[-1]=="/": ans += stack.pop()
            else: break
        stack.append(i)
    else: ans += i
    
while(stack):
    popped = stack.pop()
    if popped != "(": ans += popped

print(ans)
