
import sys
input = sys.stdin.readline
import heapq

q = []
n,m,blocks = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
times = []

max_height = max(map(max,maps))
min_height = min(map(min,maps))

for target in range(min_height,max_height+1):
    make = 0
    broke = 0
    time = 0

    for x in range(n):
        for y in range(m):
            diff = maps[x][y] - target

            if diff > 0:
                broke += diff
            elif diff < 0:
                make -= diff
            
    if broke + blocks >= make:
        time = broke*2 + make
        times.append((time, target))
answer = min(times,key=lambda x:(x[0],-x[1]))
print(answer[0],answer[1])
