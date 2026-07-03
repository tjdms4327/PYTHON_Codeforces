import sys

max_length = 0

lines = []
for line in sys.stdin.readlines():
    line = line.strip()
    n = len(line)
    
    max_length = max(max_length, n)
    lines.append((n, line))
    
print('*' * (max_length+2))

cnt = 0
for n, line in lines:
    space = (max_length-n)
    
    front = back = space//2
    if space%2:
        if cnt % 2:
            front += 1
        else:
            back += 1
        cnt += 1
    print('*' + ' '*front + line + ' '*back + '*')
    
print('*' * (max_length+2))