import sys
input = sys.stdin.readline

m, s = map(int, input().split())

if m == 1 and s == 0:
    print(0, 0)
    sys.exit()
elif s == 0:
    print(-1, -1)
    sys.exit()

if s > 9*m:
    print(-1, -1)
    sys.exit()
    
max_num  = ''
left_s = s
while left_s:
    if left_s >= 9:
        max_num += '9'
        left_s -= 9
    else:
        max_num += str(left_s)
        left_s = 0
max_num += '0' * (m - len(max_num))    
        
if max_num == -1:
    min_num = -1
else:
    min_num = list(max_num[::-1])
    if min_num[0] == '0':
        non_zero = 1
        while non_zero<m and min_num[non_zero]=='0':
            non_zero += 1
            
        min_num[non_zero] = str(int(min_num[non_zero])-1)
        min_num[0] = '1'
    min_num = ''.join(min_num)
    
print(min_num, max_num)