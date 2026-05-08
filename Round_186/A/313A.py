import sys
input = sys.stdin.readline

s = input().strip()

if int(s)>0:
    res = s
else:
    s = s[1:]
    res = min(
        s[:-2]+s[-1],
        s[:-1],
        s
    )
    res = '-'+res

print(int(res))