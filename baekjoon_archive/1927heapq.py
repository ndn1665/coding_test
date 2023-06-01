import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())
q = []
for _ in range(n):
    x = int(input().rstrip())
    
    if x >0:
        heapq.heappush(q,x)
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print('0')