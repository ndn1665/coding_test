n = int(input())

graph = [list(map(int, input())) for _ in range(n)] # 단지 맵
visited = [[False for _ in range(n)]for _ in range(n)] #방문 좌표
num_of_block = 1 # 단지 수
def dfs(x,y,graph,visited):

    global num_of_block
    if x<= -1 or x>=n or y<= -1 or y>=n : # reasonable
        return False

    if visited[x][y]:
        return False

    if graph[x][y] == 1:
        visited[x][y] = True
        dfs(x + 1, y, graph, visited)
        dfs(x - 1, y, graph, visited)
        dfs(x, y + 1, graph, visited)
        dfs(x, y - 1, graph, visited)
        graph[x][y] = num_of_block
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j,graph,visited)==True:
            num_of_block +=1



find_max = 0
for i in range(n):
    if find_max < max(graph[i]):
        find_max = max(graph[i])

num_count = [0]*(find_max+1)

for i in range(n):
    for j in range(n):
     if graph[i][j] != 0:
        num_count[graph[i][j]] += 1

print(num_of_block-1)
num_count.sort()
for i in range(find_max+1):
    if num_count[i] != 0:
        print(num_count[i])