import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n0, n1, n2 = map(int, input().split())
    
    front = ['0'] * (n0+1)
    back = ['1'] * (n2+1)
    
    # 특수 경우 처리
    if n1 == 0:
        if n0:
            print('0'*(n0+1))
            continue
        elif n2:
            print('1'*(n2+1))
            continue
    if n0 == 0:
        front = ['0']
    if n2 == 0:
        back = ['1']
    
    mid = ['1','0'] * ((n1-1)//2)
    ans = front + mid + back
    if n1 and n1%2==0:
        ans += ['0']
    
    print(''.join(ans))
        