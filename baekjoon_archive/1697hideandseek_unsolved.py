from collections import deque

n,k = map(int,input().split())
visited = [0 for _ in range(100001)]

def bfs(v):#bfs 상에서 어떤 노드를 만나면, 그 노드의 저장값은 최단거리이다. 먼저만나서 값이 저장되면 그 값이 최단거리이다.
    q = deque()
    q.append(v)
    while q:
        
        v = q.popleft()
        for i in (v-1,v+1,v*2):
            if 0<= i <=100000 and not visited[i]:
                visited[i] = visited[v] + 1 
                q.append(i)
            
            if i ==k and k!=n:
                return visited[k] 
            elif k==n:
                return 0

print(bfs(n))