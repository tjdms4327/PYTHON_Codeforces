import sys
input = sys.stdin.readline

mapping = {}

s = input().strip()
x1, y1 = ord(s[0])-ord('a'), int(s[1])

t = input().strip()
x2, y2 = ord(t[0])-ord('a'), int(t[1])

ans = []
while x1!=x2 or y1!=y2:
    
    move = ""
    
    if x1 < x2:
        move += "R"
        x1 += 1
    elif x1 > x2:
        move += 'L'
        x1 -= 1
        
    if y1 < y2:
        move += "U"
        y1 += 1
    elif y1 > y2:
        move += 'D'
        y1 -= 1
        
    ans.append(move)
    
print(len(ans))
print(*ans, sep='\n')