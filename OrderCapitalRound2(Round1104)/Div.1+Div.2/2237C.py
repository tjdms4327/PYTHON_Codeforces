import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    if A == sorted(A):
        print(max(A))
        continue
    
    stack = []
    for a in A:
        stack.append(a)
        
        while len(stack)>=2 and stack[-2] > stack[-1]:
            stack[-2] += stack[-1]
            stack.pop()
            
    print(max(stack))
    