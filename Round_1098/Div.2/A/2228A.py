import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    W = list(map(int, input().split()))
    
    cnt = W.count(0)
    
    one = W.count(1)
    two = W.count(2)
    
    temp = min(one, two)
    cnt += temp
    one -= temp
    two -= temp
    
    if one:
        cnt += one//3
    elif two:
        cnt += two//3
        
        
    print(cnt)
