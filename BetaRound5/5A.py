import sys

people = set()
ans = 0

for line in sys.stdin.readlines():
    line = line.strip()
    
    if line[0]=='+':
        people.add(line[1:])
    elif line[0]=='-':
        people.discard(line[1:]) # 보장이 없다고 할 때
    else:
        p, message = line.split(':')
        ans += len(message) * len(people)
        
print(ans)


# 없는 사람을 - 하는 경우는 없다고 보장하니
# 사람 수만 count해도 됨