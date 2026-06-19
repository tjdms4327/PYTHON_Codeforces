import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]
    #print()
    
    ans = [] # col 기준 저장됨
    for col in zip(*matrix):
        slices = list((''.join(col)).split('o'))
        
        ending_col = []
        for slice in slices:
            ending_col.append(''.join(sorted(slice, reverse=True)))
        #print(ending_col)
        ans.append('o'.join(ending_col))
        
    for row in zip(*ans):
        print(''.join(row))