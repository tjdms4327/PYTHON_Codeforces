import sys
input = sys.stdin.readline


class BIT: # 값별 등장 횟수 저장
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
        
    def add(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx&(-idx)    # 최하위 1비트만 남긴값 더하기

    def sum(self, idx): # 1~x까지 등장한 원소 수
        res = 0
        while idx:
            res += self.tree[idx]
            idx -= idx&(-idx)
        return res
    
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    bit = BIT(n)
    
    ans = 0
    processed = 0 # 지금까지 본 원소 수
    
    for a in A:
        ans += processed - bit.sum(a-1)
        
        bit.add(a, 1)
        processed += 1
        
    print(ans)