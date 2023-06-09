import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array = list(map(int,input().split()))
result = [0]*(n+1)
hap = 0
for i in range(n):
    hap +=array[i]
    result[i+1] = hap

for _ in range(m):
    a,b = map(int,input().split())
    print(result[b]-result[a-1])