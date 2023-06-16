import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i,j)
            graph[i][j] = 0
            visited[i][j] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs():
    q =deque()
    
    q.append(start)
    while q:
        x,y = q.popleft()
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=n or ny <0 or ny>=m:
                continue
            
            if visited[nx][ny] == True:
                continue
            
            visited[nx][ny] = True
            
            if graph[nx][ny] ==1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in range(n):
    for j in graph[i]:
        print(j,end =' ')
    print()