from collections import deque

n,m,answer,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

visited= [0]*(n+1)
visited[x] = 1

queue = deque([x])
while queue:
    a = queue.popleft()
    for i in graph[a]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1 + visited[a]

if (answer+1) not in visited:
    print('-1')

for i in range(len(visited)):
    if visited[i] == (answer+1):
        print(i)