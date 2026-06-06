import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    
    cand = [
        (x+y)*a, 
        abs(x-y)*a + min(x, y)*b
    ]
    print(min(cand))