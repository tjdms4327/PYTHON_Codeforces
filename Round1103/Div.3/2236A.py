import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    H = list(map(int, input().split()))
    
    standard = max(H)+1
    diff = [standard-h for h in H] 
    print(max(diff))