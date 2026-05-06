s = input().strip()

if len(s)==1:
    print(s.swapcase())
else:
    if s.isupper() or (s[0].islower() and s[1:].isupper()):
        print(s.swapcase())
    else:
        print(s)