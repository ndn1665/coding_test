n = int(input())
plans = input().split()

x , y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L','R','U','D']

for plan in plans:
    for j in range(len(types)):
        if types[j] == plan:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny
print(x,y)