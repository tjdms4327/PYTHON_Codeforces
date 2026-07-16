import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    xyz = list(map(int, input().split()))
    
    cnt = len(set(xyz))
    if cnt == 3:
        print('NO')
    elif cnt == 2:
        xyz.sort()
        if xyz[1] != xyz[2]:
            print('NO')
        else:
            print('YES')
            print(1, xyz[0], xyz[-1])
    elif cnt == 1:
        print('YES')
        print(*xyz)
    
