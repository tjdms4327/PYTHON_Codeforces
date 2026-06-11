import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    slice = list(range(1, n+1))
    ans = slice + slice[::-1] + (slice[1:]+slice[:1]) + (slice[1:]+slice[:1])[::-1]
    
    print(*ans)
