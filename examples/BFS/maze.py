from collections import deque

n,m = map(int, input().split())

graph = [[2,0,1,0,1,0],
         [1,1,1,1,1,1],
         [0,0,0,0,0,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1]]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(x,y):
    queue = deque() # queue 생성
    queue.append((x,y)) # queue에 첫번째 시작점 좌표 입력
    while queue: # queue가 채워져있으면 계속 반복
        a,b = queue.popleft() # 첫 좌표
        for i in range(4):#상하좌우에 대하여
            nx = a + dx[i] #두번째 좌표
            ny = b + dy[i]
            if nx <= -1 or nx>= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1: # 만약 두번째 좌표의 값이 1이면
                graph[nx][ny] = graph[a][b] + 1 # 두번째 좌표에 첫번째 좌표의 값에 1을 더하고
                queue.append((nx,ny)) #두번째 좌표를 queue에 넣어준다
    return graph[n-1][m-1]
print(bfs(0,0) - 1)