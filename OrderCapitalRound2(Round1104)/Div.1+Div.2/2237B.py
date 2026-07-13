import sys
input = sys.stdin.readline

def inv(arr):
    n = len(arr)
    tmp = [0]*n

    def merge(l,r):
        if r-l<=1:
            return 0
        m=(l+r)//2
        res=merge(l,m)+merge(m,r)

        i,j=l,m
        t=[]
        while i<m and j<r:
            if arr[i]<=arr[j]:
                t.append(arr[i]); i+=1
            else:
                t.append(arr[j]); j+=1
                res += m-i
        t.extend(arr[i:m])
        t.extend(arr[j:r])
        arr[l:r]=t
        return res

    return merge(0,n)


t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))


    used=[False]*n
    pos=[-1]*n

    ok=True

    for i in range(n):
        found=False
        for j in range(n):
            if not used[j] and B[j] >= A[i]:
                used[j]=True
                pos[i]=j
                found=True
                break
        if not found:
            ok=False
            break

    if not ok:
        print(-1)
        continue

    print(inv(pos))