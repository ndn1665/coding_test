n = int(input())
index = n
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
result = [0,0]

def first_check():
    start =graph[0][0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == start:
                continue
            else:return False
    result[start] = 1
    return True

def check(dx,dy):
    boundary = index//2
    start = graph[dx][dy]
    for i in range(dx,dx + boundary):
        for j in range(dy,dy + boundary):
            if graph[i][j] == start:
                continue
            else:
                return False
    result[start] +=1
    return True

while True:
    if first_check():
        break
    if index == 1:
        break
    for x in range(0,n, index//2):
        for y in range(0,n,index//2):
            if visited[x][y]:
                continue
            if check(x,y):
                for i in range(x,x+index//2):
                    for j in range(y,y+index//2):
                        visited[i][j] = True
            
    index = index//2

print(result[0])
print(result[1])