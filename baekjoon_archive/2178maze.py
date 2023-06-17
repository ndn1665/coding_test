import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[False]*(m) for _ in range(n)]


q = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q.append((0,0))
visited[0][0] = True
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx<0 or ny<0 or nx>=n or ny >= m:
            continue
        if visited[nx][ny] or graph[nx][ny] == 0:
            continue
        graph[nx][ny] = graph[x][y] +1
        visited[nx][ny] = True
        q.append((nx,ny))
print(graph[n-1][m-1])