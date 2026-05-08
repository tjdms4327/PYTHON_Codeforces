import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    
    stack = []
    for x in s:
        if x=='(':
            stack.append(x)
        else:
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(x)
                
    print(len(stack)//2)