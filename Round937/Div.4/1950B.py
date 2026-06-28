import sys
input = sys.stdin.readline

slice = ['##..', '..##']

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 1:
        print('##\n##')
        continue
    
    pattern1 = slice[0] * (n//2) + ('##' if n%2 else '')
    pattern2 = slice[1] * (n//2) + ('..' if n%2 else '')
    
    for i in range(n):
        if i%2==0:
            print(pattern1)
            print(pattern1)
        else:
            print(pattern2)
            print(pattern2)