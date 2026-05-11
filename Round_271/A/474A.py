import sys
input = sys.stdin.readline

keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
mapping = {'R': -1 , 'L': 1}

swift = mapping[input().strip()]
s = input().strip()

res = ''
for x in s:
    real_idx = keyboard.index(x) + swift
    if real_idx > len(keyboard)-1:
        real_idx = 0
    
    res += keyboard[real_idx]
    
print(res)
        