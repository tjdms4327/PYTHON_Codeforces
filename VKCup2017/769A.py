import sys
input = sys.stdin.readline

n = int(input())
years = list(map(int, input().split()))
years.sort()

print(years[n//2])
