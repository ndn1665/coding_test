import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split())

distance = [INF] * (n+1)
distance[start] = 0
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(start,0))

    while q:
        now, dist = heapq.heappop(q)
        if visited[now] == True:
            continue
        visited[now] = True

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

dijkstra(start)

