import sys
input = sys.stdin.readline

n, vb, vs = map(int, input().split())
X = list(map(int, input().split()))
xu, yu = map(int, input().split())

double_y = yu**2

INF = float('inf')
best = [-1, INF, INF] # [정류장번호, 거리, 시간]
for i in range(n-1, 0, -1):
    xi = X[i]
    bus_time = xi/vb
    
    dist = ((xu - xi)**2 + double_y)**0.5
    tot_time = bus_time + dist/vs
    
    if best[-1] > tot_time:
        best = (i+1, dist, tot_time)
    elif tot_time == best[2] and dist < best[1]:
        best = (i+1, dist, tot_time)
        
print(best[0])