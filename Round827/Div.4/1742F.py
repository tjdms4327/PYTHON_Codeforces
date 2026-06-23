import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    q = int(input())
    
    s_acnt, t_acnt = 1, 1
    s_other, t_other = 0, 0
    
    for _ in range(q):
        d, k, x = input().strip().split()
        k = int(k)
        
        cnt = x.count('a')*k
        other = len(x)*k - cnt

        if d == '1':
            s_acnt += cnt
            s_other += other
        else:
            t_acnt += cnt
            t_other += other
            
        if t_other: # 맨 앞에 넣기
            print('YES')
        else:
            if s_acnt<t_acnt and s_other==0:
                print('YES')
            else:
                print('NO')