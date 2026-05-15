import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p1, p2, p3 = map(int, input().split())

    if (p1+p2+p3)%2:
        print(-1)
        continue
    
    game = (p1+p2+p3) // 2
    if (p1+p2) < p3:
        need = p3-p1-p2
        game -= need//2
        
    print(game)