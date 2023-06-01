from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i,j))
            
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx<0 or ny >= n or ny<0:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
            else:
                if graph[nx][ny] <= graph[x][y] + 1 :
                    continue
                graph[nx][ny] = min(graph[nx][ny], graph[x][y] + 1)
                q.append((nx,ny))
bfs()
for i in range(m):
    if 0 in graph[i]:
        print('-1')
        break
else:
    print(max(map(max,graph))-1)