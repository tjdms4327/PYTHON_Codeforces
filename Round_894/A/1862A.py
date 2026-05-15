import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]
    
    vika = ''
    for col in zip(*matrix):
        if len(vika)==0:
            if 'v' in col:
                vika += 'v'
        elif len(vika)==1:
            if 'i' in col:
                vika += 'i'
        elif len(vika)==2:
            if 'k' in col:
                vika += 'k'
        elif len(vika)==3:
            if 'a' in col:
                vika += 'a'
                
    if vika == 'vika':
        print('YES')
    else:
        print('NO')