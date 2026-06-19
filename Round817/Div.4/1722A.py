import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if n == 5 and sorted(s) == sorted("Timur"):
        print("YES")
    else:
        print("NO")