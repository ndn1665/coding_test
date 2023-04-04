n,m = map(int, input().split())
x,y,direction = map(int, input().split())

gmmap = [[1,1,1,1],
         [1,0,0,1],
         [1,1,0,1],
         [1,1,1,1]]

visited = [[0 for _ in range(4)]for _ in range(4)]
visited[x][y] = 1
d = [0,1,2,3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
move = 0
count = 1
while True:
    for i in range(4):
        move +=1
        move = move%4
        nx = x + dx[move]
        ny = y + dy[move]
        if visited[nx][ny] == 1 or gmmap[nx][ny] == 1 :
            nx = 0
            ny = 0
            continue
        else:
            count +=1
            visited[nx][ny] = 1
            x,y = nx,ny
            direction = move
            break
    else:
        break
print(count)