import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    
    m = int(input())
    b = input().strip()
    c = input().strip()
    
    front_reverse, back = '',''
    for i in range(m):
        if c[i] == 'V':
            front_reverse += b[i]
        else:
            back += b[i]
            
    print(front_reverse[::-1] + a + back)
