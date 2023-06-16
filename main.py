import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    inline = list(map(int, input().split()))
    for j in range(1,len(inline),2):
        if inline[j] == -1:
            break
        a,b = inline[j],inline[j+1]
        graph[i].append((a,b))

for i in range(1,n+1):
    print(graph[i])
