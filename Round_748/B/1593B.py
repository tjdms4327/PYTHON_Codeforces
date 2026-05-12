import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().strip()
    
    cnt = 10**9
    
    # 마지막 자리가 25, 50, 75, 00 중 하나
    five = n.rfind('5')
    for i in range(five-1, -1, -1):
        if n[i] in '27':
            cnt = (len(n)-1 - five) + (five-1 - i)
            break
    
    zero = n.rfind('0')
    for i in range(zero-1, -1, -1):
        if n[i] in '50':
            cnt = min(cnt, (len(n)-1 - zero) + (zero-1 - i))
            break
        
    print(cnt)