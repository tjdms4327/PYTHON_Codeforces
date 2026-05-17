import sys
input = sys.stdin.readline

n, t = map(int, input().split())

t_len = len(str(t))

if t == 10 and n == 1:
    print(-1)
    sys.exit()
    
res = str(t) + '0'*(n-t_len)
print(int(res))