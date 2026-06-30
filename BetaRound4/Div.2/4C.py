import sys
input = sys.stdin.readline

DB = {}

t = int(input())
for _ in range(t): 
    s = input().strip()
    if s not in DB:
        DB[s] = 1
        print('OK')
    else:
        k = DB[s]
        while s+str(k) in DB:
            k += 1
        new = s + str(k)
        print(new)
        
        DB[s] = k + 1
        DB[new] = 1
        