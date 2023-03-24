game_map = [[1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]]

array = [[0] * 4 for _ in range(4)]

x, y, d = map(int, input().split())  # 1 1 0


# d에 대하여
# 0 북 #1 서 #2 동 #3 남

def turn():
    global d
    d += 1
    if d == 4:
        d = 0


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 1
limit = 0
array[x][y] = 1  # 초기 위치 방문 처리
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]

    if game_map[nx][ny] == 0 and array[nx][ny] == 0:
        array[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        limit = 0
        continue
    else:
        limit += 1

    if limit == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

print(count)