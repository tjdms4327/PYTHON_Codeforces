import sys
input = sys.stdin.readline

n = list(input().strip())
m = list(input().strip())

n.sort()
if n[0] == '0':
    for i in range(1, len(n)):
        if n[i] != '0':
            n[0], n[i] = n[i], n[0]
            break
        
if n == m:
    print('OK')
else:
    print('WRONG_ANSWER')